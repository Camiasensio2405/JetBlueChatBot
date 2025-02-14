from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "flight": "I can help you with flight bookings and cancellations.",
        "hotel": "We provide hotel accommodations if your flight is delayed.",
        "bye": "Safe travels! Let me know if you need anything else."
    }
    return responses.get(user_input.lower(), "I'm not sure how to answer that. Try asking about flights or hotels!")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
