from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
app.config["DB"] = client["smartspend_db"]

from routes.transactions import transactions_bp
app.register_blueprint(transactions_bp)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)
