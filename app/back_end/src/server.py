from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def run():
    app.run(host='localhost', port=5500, debug=True)
