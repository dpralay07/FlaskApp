from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello! Welcome to Azure."

@app.route("/home")
def home():
    return "Hello! Welcome to the Home page of GSBot."


if __name__ == "__main__":
    app.run()
