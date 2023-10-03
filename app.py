from flask import Flask, request, jsonify

app = Flask(__name__)

def sanitize_input(prompt, user):
    # Check if both "prompt" and "user" are strings
    if not isinstance(prompt, int) or not isinstance(user, str):
        return False
    return True

@app.route('/process', methods=['POST'])
def process_request():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        user = data.get('user')

        # Check if "prompt" and "user" are strings
        if not sanitize_input(prompt, user):
            return jsonify({"error": "Invalid input. Both prompt and user should be strings."}), 400

        # For now, we'll return a success message.
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
