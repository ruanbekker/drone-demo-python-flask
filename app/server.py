from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'ok'}), 200

if __name__ == '__main__':
    app.run()
