from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config.settings import Config
from database.mongo import init_mongo
from middleware.error_handler import register_error_handlers
from utils.logger import configure_logging
from routes.auth_routes import auth_bp
from routes.predict_routes import predict_bp
from routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    JWTManager(app)
    Limiter(get_remote_address, app=app, default_limits=[app.config["RATE_LIMIT"]])

    configure_logging(app)
    init_mongo(app)
    register_error_handlers(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(predict_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["FLASK_ENV"] == "development")
