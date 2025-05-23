from flask import Flask, jsonify,  send_from_directory
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('static' , 'index.html')

@app.route('/api/message', methods=['GET'])
def message():
    return jsonify({"message": "Hello from the Flask backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
