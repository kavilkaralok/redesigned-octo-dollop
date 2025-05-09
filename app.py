from flask import Flask, request, jsonify
import logging
import os

# Create logs directory if it doesn't exist
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
    return "✅ Flask log server is running!"

@app.route("/log", methods=["POST"])
def log_something():
    if not request.is_json:
        logging.warning("Received non-JSON request")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Extract message and optional log level
    message = data.get("message", "No message provided")
    level = data.get("level", "INFO").upper()

    # Log with the appropriate level
    if level == "DEBUG":
        logging.debug(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "CRITICAL":
        logging.critical(message)
    else:
        logging.info(message)

    return jsonify({"status": "logged", "level": level, "message": message}), 200

# Entry point
if __name__ == "__main__":
    logging.info("Starting Flask log server...")
    app.run(host="0.0.0.0", port=5000, debug=True)

