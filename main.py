from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Render PaaS! Version 1 - Cloud Computing Group Project"
