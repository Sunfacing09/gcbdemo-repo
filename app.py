from flask import Flask, render_template, request
import os
import socket

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    html = "<h3>Hello, World! It worked Again</h3>"
    return render_template('index.html')


@app.route("/<promotion>", methods=['GET'])
def promotion(promotion="Nothing"):
    promotion = request.args.get('promotion', promotion)
    html = "<h3>It's promotion page</h3>"
    return promotion




if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)