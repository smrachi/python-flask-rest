from flask import Flask
import os, sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    cwd = os.getcwd()
    mydict = {
        'cwd': cwd,
        'hello': 'Hello World!'
    }
    return mydict

@app.route("/run/wireshark")
def run_wireshark():
    os.system("wireshark")

@app.route("/close/wireshark")
def close_wireshark():
    os.system("pkill wireshark")

if __name__ == "__main__":
    app.run(port=8080)