from flask import Flask, request, jsonify
from .operations import *

app = Flask(__name__)


@app.route("/add", methods=["GET"])
def add_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = add(a, b)
    return jsonify({"result": result})


@app.route("/subtract", methods=["GET"])
def subtract_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = subtract(a, b)
    return jsonify({"result": result})


@app.route("/multiply", methods=["GET"])
def multiply_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = multiply(a, b)
    return jsonify({"result": result})


@app.route("/divide", methods=["GET"])
def divide_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = divide(a, b)
    return jsonify({"result": result})
