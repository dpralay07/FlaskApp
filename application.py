from flask import Flask, jsonify
import jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello! Welcome to Azure Application of GS Bot."

@app.route("/home")
def home():
    return jsonify({'status': 'success', 'description': 'Endpoint is working fine.'})


if __name__ == "__main__":
    app.run()
