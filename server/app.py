from flask import Flask, jsonify, request
from flask_cors import CORS
import rpyParser

app = Flask(__name__)
projectName = 'test'
CORS(app)

@app.route("/testDialogues")
def testDialogues():
    proj = rpyParser.getProjectJson(projectName)
    data = {'dialogues': proj['scenes']}
    return jsonify(data)

@app.route("/testProject")
def testProject():
    proj = rpyParser.getProjectJson(projectName)
    data = {'scenes': proj['scenes']}
    return jsonify(data)

@app.route("/saveScene", methods = ['POST'])
def saveScene():
    if request.method == 'POST':
        scene = request.get_json(force=True)
        if (rpyParser.overWriteScene(projectName,scene)):
            return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = {}), 200
        else:
            return jsonify(isError = False,
                            message = "Failed",
                            statusCode = 200,
                            data = {}), 200

if __name__ == '__main__':
    app.run(debug=True)