# Fetus AI - A foundational AI script for natural language understanding and generation

import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Fetus AI Configurations
openai.api_key = "ajdbn132ajslka00018134aslkahkslash"  # Replace with your OpenAI API Key
model_name = "gpt-4"  # Define the AI model to use

# Default route for status check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Fetus AI is running!", "version": "1.0"})

# Route for processing user input
@app.route("/process", methods=["POST"])
def process_input():
    try:
        # Get user input from POST request
        data = request.json
        user_input = data.get("input", "")
        if not user_input:
            return jsonify({"error": "Input is required"}), 400

        # Generate AI response
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are Fetus AI, an assistant designed to help with any query."},
                {"role": "user", "content": user_input}
            ]
        )
        ai_response = response['choices'][0]['message']['content']

        return jsonify({"input": user_input, "response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add a development mode if needed
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
