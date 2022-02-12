from flask import Flask, render_template, request
import os
import socket

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    html = "<h3>Hello, World! It worked Again</h3>"
    rewards = []
    for i in range(1, 11):
        rewards.append(i)
    return render_template('index.html', rewards=rewards)


@app.route("/promotion", methods=['GET'])
def promotion(reward="Nothing"):
    reward = request.args.get('reward', reward)
    return render_template('promotion.html', reward=reward)




if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8080)