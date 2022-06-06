from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import rpyParser

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testKey'
app.config['UPLOAD_FOLDER'] = 'static/files'
CORS(app)

projectName = 'test'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

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
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__))
                                ,app.config['UPLOAD_FOLDER']
                                ,secure_filename(file.filename)))
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