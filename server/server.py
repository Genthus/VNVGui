from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import pathlib
import os
import rpyParser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testKey'
app.config['UPLOAD_FOLDER'] = 'files'
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

@app.route('/createProject')
def createProject():
    projectName = request.args.get('name')
    if rpyParser.createProject(projectName):
        rpyParser.discoverProjects()
        return jsonify(isError = False,
                        message = "Project created",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error creating project",
                        statusCode = 100,
                        data = {}), 100

@app.route('/deleteProject')
def deleteProject():
    projectName = request.args.get('name')
    if rpyParser.deleteProject(projectName):
        return jsonify(isError = False,
                        message = "Project deleted",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error deleting project",
                        statusCode = 100,
                        data = {}), 100

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

@app.route('/createScene')
def createScene():
    projectId = request.args.get('projectId')
    newSceneName = request.args.get('name')
    if (rpyParser.createNewScene(projectId,newSceneName)):
        return jsonify(isError = False,
                        message = "Scene created",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error creating scene",
                        statusCode = 100,
                        data = {}), 100

@app.route('/deleteScene')
def deleteScene():
    projectId = request.args.get('projectId')
    sceneId = request.args.get('id')
    if (rpyParser.deleteScene(int(projectId),int(sceneId))):
        return jsonify(isError = False,
                        message = "Scene deleted",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error deleting scene",
                        statusCode = 100,
                        data = {}), 100


@app.route('/getResourceList')
def getResourceList():
    projectId = request.args.get('projectId')
    data = rpyParser.getResourceListById(projectId)
    if data:
        return jsonify(data)
    return jsonify(isError = True,
                    message = "Error getting resourceList",
                    statusCode = 100,
                    data = {}), 100

@app.route("/getFile")
def getFile():
    projectId = request.args.get('projectId')
    fileDir = request.args.get('fileDir')
    resources = rpyParser.getResourceListById(projectId)
    if resources:
        if os.path.isfile(fileDir):
            return send_file(fileDir)
    return jsonify(isError = True,
                    message = "Error sending file",
                    statusCode = 100,
                    data = {}), 100

@app.route("/uploadResource", methods= ['POST'])
def uploadResource():
    form = UploadFileForm()
    if form:
        file = form.file.data
        projectId = request.args.get('projectId')
        projectDir = os.path.join(os.path.abspath(os.path.dirname(__file__))
                                ,app.config['UPLOAD_FOLDER']
                                ,'project_' + str(projectId))
        projectDir = os.path.join(rpyParser.filesFolder, 'project_' + (str(projectId)))
        if not os.path.isdir(projectDir):
            os.mkdir(projectDir)
        hashedFileName = str(hash(projectName + form.name.data + form.type.data)) + pathlib.Path(file.filename).suffix
        file.save(os.path.join(projectDir,secure_filename(hashedFileName)))
        rpyParser.saveResourceFile(projectId, form.name.data, form.type.data, hashedFileName, os.path.join(projectDir,secure_filename(hashedFileName)))
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
            rpyParser.setJumps(projectId)
            return jsonify(isError = False,
                            message = "Success",
                            statusCode = 200,
                            data = {}), 200
        else:
            return jsonify(isError = True,
                            message = "Failed to save scene",
                            statusCode = 100,
                            data = {}), 200

@app.route("/parse")
def parseProject():
    projectId = request.args.get('projectId')
    if (rpyParser.writeScriptByProjectId(int(projectId))):
        return jsonify(isError = False,
                        message = "parsing completed",
                        statusCode = 200,
                        data = {}), 200
    else:
        return jsonify(isError = True,
                        message = "Error parsing project",
                        statusCode = 100,
                        data = {}), 100



if __name__ == '__main__':
    isDebug = False
    rpyParser.setup(isDebug)
    app.run(debug=isDebug)