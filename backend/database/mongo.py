from pymongo import MongoClient

client = None
db = None


def init_mongo(app):
    global client, db
    client = MongoClient(
        app.config["MONGO_URI"],
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db = client[app.config["MONGO_DB_NAME"]]
    ensure_indexes()


def get_db():
    return db


def ensure_indexes():
    database = get_db()
    database.users.create_index("email", unique=True)
    database.scan_history.create_index("user_id")
    database.scan_history.create_index("created_at")
