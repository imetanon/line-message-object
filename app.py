from flask import Flask, request, jsonify, Response
import json


app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, Flask on heroku'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)