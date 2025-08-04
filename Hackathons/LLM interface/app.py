from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from cerebras.cloud.sdk import Cerebras
import os

app = Flask(__name__)
CORS(app)

# Configure Cerebras
api_key = os.environ.get("CEREBRAS_API_KEY", "csk-5hef36cn4ewpnxex2jxnkrn5vnkhtrcyyw9fth3r8emewnmp")
client = Cerebras(api_key=api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            model="llama-4-scout-17b-16e-instruct",
            max_completion_tokens=500,
            temperature=0.7,
            top_p=0.95
        )

        # Add better error handling for the response structure
        if response.choices and len(response.choices) > 0 and response.choices[0].message:
            return jsonify({
                "response": response.choices[0].message.content
            })
        else:
            return jsonify({"error": "Invalid response from Cerebras API"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
