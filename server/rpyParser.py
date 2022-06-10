#rpy parser
import os
import shutil
import json

projectsFolder = "../projects/"
baseProjectFolder = "./defs/base/"

def getProjectJson(proJname):
    with open(projectsFolder+proJname+"/project.json", 'r') as f:
        return json.load(f)

def overWriteScene(projName, scene):
    with open(projectsFolder+projName+"/project.json", 'r+') as f:
        data = json.load(f)
        if (data["scenes"][scene["id"]]):
            data["scenes"][scene["id"]] = scene
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            return True
        else:
            print("Scene " + scene.name + " not found, overwrite failed")
            return False

def saveResourceFile(projName, name, type, fileName):
    with open(projectsFolder+projName+"/project.json", 'r+') as f:
        data = json.load(f)
        if 'resources' not in data:
            data["resources"] = {}
        if type not in data["resources"]:
            data["resources"][type] = {}

        if name in data["resources"][type]:
            print("data exists")
        else:
            data["resources"][type][name] = {'name': name,'type': type,'fileName': fileName}
        f.seek(0)
        f.truncate()
        json.dump(data, f)
        return True

# Finds jump instructions inside scenes and adds them to a key in the root of project.json
def setJumps(projName):
    with open(projectsFolder+projName+"/project.json", 'r+') as f:
        data = json.load(f)

        jumps = []
        if 'scenes' not in data:
            data['scenes'] = {}
        for scene in data['scenes']:
            if 'lines' in scene:
                for line in scene['lines']:
                    if line['type'] == 'jump':
                        jumps.append({'source': scene['name'], 'location': line['id'], 'destination': line['text']})

        print(jumps)
        if 'jumps' not in data:
            data['jumps'] = []
        data['jumps'] = jumps

        f.seek(0)
        f.truncate()
        json.dump(data, f)
        return True


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
        projFileExists = os.exists(self.baseDirectory + "project.json")
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
    if not os.exists(projectsFolder+name):
        shutil.copytree(baseProjectFolder,projectsFolder+name)
        newProj = Project(name)
        newProj.setDirectory(projectsFolder+name+'/')
        return newProj
    else:
        print("Project with that name already exists")

def openProject(name):
    if os.exists(projectsFolder+name):
        return Project(name)

def discoverProjects():
    projects = []

    for root, subdirectories, files in os.walk(projectsFolder):
        for subdirectory in subdirectories:
            if os.isdir(subdirectory):
                if 'project.json' in subdirectory.os.listdir():
                    with open(subdirectory + '/project.json', "r") as f: 
                        data = json.load(f)
                        if 'projectName' in data:
                            projects.append({'name': data['projectName'], 'path': subdirectory})
                            
    with open(projectsFolder + '/projects.json', "r") as f: 
        data = json.load(f)
        if 'projects' not in data:
            data['projects'] = []
        data['projects'] = projects
        f.seek(0)
        f.truncate()
        json.dump(data, f)
    

def getProjects():
    with open(projectsFolder + '/projects.json', "r") as f: 
        return json.load(f)


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