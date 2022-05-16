from flask import Flask, jsonify
import random
import rpyParser

app = Flask(__name__)
projectName = 'test'

@app.route("/testDialogues")
def testDialogues():
    proj = rpyParser.getProjectJson('test')
    data = {'dialogues': proj['scenes']}
    return jsonify(data)

@app.route("/testProject")
def testProject():
    proj = rpyParser.getProjectJson('test')
    data = {'scenes': proj['scenes']}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)