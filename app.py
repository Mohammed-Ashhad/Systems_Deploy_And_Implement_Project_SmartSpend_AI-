from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://host.docker.internal:27017/")
client = MongoClient(MONGO_URI)
db = client["smartspend_db"]

# Store db inside app config
app.config["DB"] = db

from routes.transactions import transactions_bp
app.register_blueprint(transactions_bp)

from routes.ai_analysis import ai_bp
app.register_blueprint(ai_bp)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)