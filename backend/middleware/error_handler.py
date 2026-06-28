from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad request", "details": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Route not found"}), 404

    @app.errorhandler(429)
    def rate_limited(error):
        return jsonify({"error": "Rate limit exceeded", "details": str(error)}), 429

    @app.errorhandler(Exception)
    def internal_error(error):
        app.logger.exception("Unhandled exception: %s", error)
        return jsonify({"error": "Internal server error"}), 500
