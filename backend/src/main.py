from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_route():
    return {"message": "Welcome to the Flask server!"}

@app.route('/test', methods=['GET'])
def test_route():
    return {"message": "Flask server is running!"}

@app.route('/ask', methods=['POST'])

def ask_gpt():
    data = request.get_json()

    if not data or 'prompt' not in data or not isinstance(data['prompt'], str) or not data['prompt'].strip():
        return jsonify({"error": "Invalid or missing 'prompt'. Please provide a non-empty string."}), 400

    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    try:
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)