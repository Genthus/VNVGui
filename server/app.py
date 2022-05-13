from flask import Flask, jsonify
import random
import rpyParser

app = Flask(__name__)
projectName = 'test'

@app.route ("/")
def index():
    return "<p>w!</p>"

@app.route ("/number")
def ranNum():
    data = {'number': random.randrange(1,1000,1)}
    return jsonify(data)

@app.route("/testDialogues")
def testDialogues():
    proj = rpyParser.getProjectJson('test')
    data = {'dialogues': proj['scenes']}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)