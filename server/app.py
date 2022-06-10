from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import pathlib
import os
import rpyParser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testKey'
app.config['UPLOAD_FOLDER'] = 'static/files'
CORS(app)

projectName = 'test'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    type = FileField("type")
    name = FileField("name")
    submit = SubmitField("Upload File")

@app.route("/projects")
def listProjects():
    rpyParser.discoverProjects()
    data = rpyParser.getProjects()
    return jsonify(data)

@app.route("/project")
def getProject():
    projectId = request.args.get('id')
    projectData = rpyParser.getProjectJsonById(projectId)
    return jsonify(projectData)

@app.route('/getScene')
def getScene():
    projectId = request.args.get('projectId')
    sceneId = request.args.get('sceneId')
    scene = rpyParser.getSceneById(projectId, sceneId)
    if scene:
        return jsonify(scene)
    return jsonify(isError = True,
                    message = "Error getting scene",
                    statusCode = 100,
                    data = {}), 100

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

@app.route("/uploadResource", methods= ['POST'])
def uploadResource():
    form = UploadFileForm()
    if form:
        file = form.file.data
        fileCopy = form.file.data
        hashedFileName = str(hash(projectName + form.name.data + form.type.data)) + pathlib.Path(file.filename).suffix
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__))
                                ,app.config['UPLOAD_FOLDER']
                                ,secure_filename(hashedFileName)))
        rpyParser.saveResourceFile(projectName, form.name.data, form.type.data, hashedFileName)
        return jsonify(isError = False,
                        message = "File Uploaded",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error uploading file",
                        statusCode = 100,
                        data = {}), 100

@app.route("/saveScene", methods = ['POST'])
def saveScene():
    if request.method == 'POST':
        projectId = request.args.get('projectId')
        sceneId = request.args.get('sceneId')
        scene = request.get_json(force=True)
        if (rpyParser.overWriteSceneById(int(projectId),int(sceneId),scene)):
            rpyParser.setJumps(projectName)
            return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = {}), 200
        else:
            return jsonify(isError = True,
                            message = "Failed to save scene",
                            statusCode = 100,
                            data = {}), 200

if __name__ == '__main__':
    app.run(debug=True)