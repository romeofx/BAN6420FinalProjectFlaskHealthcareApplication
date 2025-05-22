import os
from flask import Flask, jsonify
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")

# Get MongoDB URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Initialize Mongo client
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5 sec timeout
    db = client.get_database()  # Gets default DB from URI
    # Try pinging the server to confirm connection
    client.admin.command('ping')
    print("MongoDB connection established successfully.")
except errors.ServerSelectionTimeoutError as err:
    print(f"MongoDB connection failed: {err}")
    db = None

@app.route('/')
def home():
    if db is None:
        return jsonify({"error": "Database connection not established."}), 500
    return jsonify({"message": "Welcome to the Survey App!", "database": str(db.name)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
