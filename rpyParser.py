#rpy parser
from os.path import exists
import shutil
import json

projectsFolder = "./projects/"
baseProjectFolder = "./defs/base/"

class Project:
    name = ""
    baseDirectory = ""
    projectObject = ''
    projectScenes = []

    def __init__(self, name):
        self.name = name
        self.baseDirectory = projectsFolder + name + "/"
    
    def setDirectory(self, directory):
        self.baseDirectory = directory

    def writeScriptToFile(self):
        output = ''
        for scene in self.projectScenes:
            output += scene.writeScene()
        try:
            with open(self.baseDirectory +"game/script.rpy", 'w') as f:
                f.write(output)
                print("Wrote script to: "+ self.baseDirectory + "script.rpy")
        except FileNotFoundError:
            print('The file does not exist.\n')
    
    def parseProjectJSON(self):
        # Load json file
        projFileExists = exists(self.baseDirectory + "project.json")
        if projFileExists:
            with open(self.baseDirectory+"project.json", "r") as f: 
                self.ProjectObject = json.load(f)
                print("Project JSON file loaded")
        else:
            print("Project JSON file was not found\n")
            return

        # Convert scenes
        for scene in self.ProjectObject["scenes"]:
            self.projectScenes.append(RpyScene(scene,self.ProjectObject["scenes"][scene]))
        self.ProjectObject["scenes"]
        

def createProject(name):
    if not exists(projectsFolder+name):
        shutil.copytree(baseProjectFolder,projectsFolder+name)
        newProj = Project(name)
        newProj.setDirectory(projectsFolder+name+'/')
        return newProj
    else:
        print("Project with that name already exists")

def openProject(name):
    if exists(projectsFolder+name):
        return Project(name)


class RpyScene:
    name = "tempName"
    sceneContent = ["tempItem", "tempItem2"]

    def __init__(self, name, sceneContent):
        self.name = name
        self.sceneContent = sceneContent
    
    def writeScene(self):
        s = "label %s:\n"%self.name
        for l in self.sceneContent:
            s += "    %s\n"%l
        return s

#testProject = Project("test")
proj = openProject("test2")
proj.parseProjectJSON()
proj.writeScriptToFile()
#testScene = RpyScene("start", ['\"hello\"', '\"goodbye\"'])
#testProject.writeScriptToFile([testScene])