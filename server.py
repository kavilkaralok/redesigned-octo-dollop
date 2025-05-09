from flask import Flask, request
import logging
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Set up logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Hello, Flask server is running!"

@app.route("/log", methods=["POST"])
def log_something():
    data = request.get_json()
    message = data.get("message", "No message provided")
    logging.info(f"Received log: {message}")
    return {"status": "logged", "message": message}, 200

if __name__ == "__main__":
    logging.info("Starting server...")
    app.run(debug=True)
