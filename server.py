from flask import Flask, request, render_template, Response, jsonify
import json
from random import randint
from test import predict

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
	if request.method == "POST":
		print(request)
		response = json.loads(request.data)
		#print(response["number"])
		pred = predict(response["number"])
		return jsonify({"message": pred})


if __name__ == "__main__":
	app.run(debug=True, port=4040)