import time
from flask import Flask, jsonify, request, redirect
import requests
import time
from flask import Flask, jsonify, request, redirect, session
import requests

app = Flask(__name__)


@app.route("/api/time", methods=["GET"])
def get_current_time():
    return {"time": time.time()}

@app.route("/api/send-message", methods=["POST"])
def send_message():
    data = request.get_json()
    message = data.get("name", "")
    return jsonify({"responseMessage": f"Hello {message}"})
