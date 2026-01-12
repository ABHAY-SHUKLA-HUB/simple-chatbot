# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    
    # Simple response logic
    if not user_message:
        return jsonify({"reply": "Please say something!"})
    
    if 'hello' in user_message.lower():
        reply = "Hello! How can I help you?"
    elif 'bye' in user_message.lower():
        reply = "Goodbye! Have a nice day!"
    else:
        reply = "Sorry, I don't understand that yet."
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
