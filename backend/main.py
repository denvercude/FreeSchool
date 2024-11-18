from flask import Flask, request, jsonify  # Import Flask tools for handling requests and JSON responses.
from dotenv import load_dotenv  # Import dotenv to load environment variables from .env.
import os  # Import os to access environment variables.
from src.utils.ai_utils import generate_response # Import the AI utility function.

# Load environment variables
load_dotenv()  # Load environment variables from the .env file.

# Create Flask app
app = Flask(__name__)  # Create the Flask app instance.

@app.route('/', methods=['GET'])  # Define a root route ('/') that responds to GET requests.
def root_route():
    return {"message": "Welcome to the Flask server!"}  # Respond with a simple JSON welcome message.

@app.route('/test', methods=['GET'])  # Define a route '/test' that responds to GET requests.
def test_route():
    return {"message": "Flask server is running!"}  # Respond with a simple JSON message.

@app.route('/ask', methods=['POST'])  # Define a route '/ask' that responds to POST requests.
def ask_gpt():
    data = request.get_json()  # Parse the JSON body of the POST request.

    # Validate that the JSON data contains a non-empty 'prompt'.
    if not data or 'prompt' not in data or not isinstance(data['prompt'], str) or not data['prompt'].strip():
        return jsonify({"error": "Invalid or missing 'prompt'. Please provide a non-empty string."}), 400

    prompt = data['prompt'].strip()  # Safely extract and strip whitespace from the 'prompt'.

    # Call the AI utility function
    response = generate_response(prompt)  # Get the AI-generated response.
    if response.startswith("Error"):  # Check if an error occurred.
        return jsonify({"error": response}), 500  # Return the error message with a 500 status code.

    return jsonify({"response": response})  # Return the GPT response in JSON format.

if __name__ == "__main__":  # If the script is run directly, start the Flask server.
    app.run(debug=True)  # Start the server in debug mode for easy troubleshooting.
