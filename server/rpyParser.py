#rpy parser
import os
import shutil
import json

# Main folder where project directories and projects.json is stored
projectsFolder = "../projects"
# Directory for base project
baseProjectFolder = "./.defs/base"
filesFolder = "./static/files"

def setup(debug):
    if (not debug):
        p = os.path.join(os.getcwd(),'config.json')
        if (not os.path.exists(p)):
            createProjectFolder(debug)
            createFilesFolder(debug)
            with open(p, 'w') as f:
                data = {
                    'projectsFolder' : os.path.join(os.getcwd(),'./projects'),
                    'filesFolder' : os.path.join(os.getcwd(), './files')
                }
                json.dump(data,f)
            return True
        else:
            with open(p,'r') as f:
                data = json.load(f)
                global projectsFolder
                projectsFolder = data['projectsFolder']
                global filesFolder
                filesFolder = data['filesFolder']

def createProjectFolder(debug):
    if (not debug):
        p = os.path.join(os.getcwd(),'projects')
        if (not os.path.exists(p)):
            os.mkdir(p)
        if (not os.path.exists(os.path.join(p,'projects.json'))):
            with open(os.path.join(p,'projects.json'), 'w') as f:
                f.write('{}')
            return True
    return False

# Startup
def createFilesFolder(debug):
    if (not debug):
        p = os.path.join(os.getcwd(),'files')
        if (not os.path.exists(p)):
            os.mkdir(p)
        return True
    return False

# Searches for a project with proJname in the projects folder, returns project.json
def getProjectJson(proJname):
    with open(os.path.join(projectsFolder,proJname,"project.json"), 'r') as f:
        return json.load(f)

# Searches through projects.json and returns the project.json
def getProjectJsonById(id):
    projects = getProjects()
    projectPath = ''
    project = projects['projects'][int(id)]
    if project:
        projectPath = project['path']
    if projectPath != '':
        with open(os.path.join(projectPath,'project.json'), 'r') as f:
            return json.load(f)
    print('Error loading project with id:' + id + ' at path: ' + projectPath)
    return False

def saveProjectJsonById(id, data):
    projects = getProjects()
    projectPath = ''
    project = projects['projects'][int(id)]
    if project:
        projectPath = project['path']
    if projectPath != '':
        with open(os.path.join(projectPath,'project.json'), 'w') as f:
            f.seek(0)
            f.truncate()
            json.dump(data,f)
            return True
    return False

# Overwrites scene object by its index
def createNewScene(projId, name):
    projects = getProjects()
    projectPath = ''
    project = projects['projects'][int(projId)]
    if project:
        projectPath = project['path']
    if projectPath != '':
        with open(os.path.join(projectPath,'project.json'), 'r+') as f:
            data = json.load(f)
            if (data["scenes"]):
                newScene = {"id": len(data["scenes"]), "name": name, "lines": []}
                data["scenes"].append(newScene)
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                return True
            else:
                return False

# Overwrites scene object by its index
def overWriteSceneById(projId, sceneId, scene):
    projects = getProjects()
    projectPath = ''
    project = projects['projects'][projId]
    if project:
        projectPath = project['path']
    if projectPath != '':
        with open(os.path.join(projectPath,'project.json'), 'r+') as f:
            data = json.load(f)
            if (data["scenes"][scene["id"]]):
                data["scenes"][scene["id"]] = scene
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                return True
            else:
                return False

def deleteScene(projId, sceneId):
    projects = getProjects()
    projectPath = ''
    project = projects['projects'][projId]
    if project:
        projectPath = project['path']
    if projectPath != '':
        with open(os.path.join(projectPath,'project.json'), 'r+') as f:
            data = json.load(f)
            if (data["scenes"][sceneId]):
                del data["scenes"][sceneId]
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                return True
            else:
                return False
# Takes data of new resource file and adds it to project.json
def saveResourceFile(projId, name, type, fileName, fileDir):
    data = getProjectJsonById(projId)
    if 'resources' not in data:
        data["resources"] = {}
    if type not in data["resources"]:
        data["resources"][type] = {}

    if name in data["resources"][type]:
        print("data exists")
    else:
        data["resources"][type][name] = {'name': name,'type': type,'fileName': fileName, 'fileDir': fileDir}
    
    if saveProjectJsonById(projId, data):
        return True
    return False

# Finds jump instructions inside scenes and adds them to a key in the root of project.json
def setJumps(projId):
    data = getProjectJsonById(projId)
    if data:
        jumps = []
        if 'scenes' not in data:
            data['scenes'] = {}
        for scene in data['scenes']:
            if 'lines' in scene:
                for line in scene['lines']:
                    if line['type'] == 'jump':
                        jumps.append({'source': scene['name'], 'location': line['id'], 'destination': line['text']})

        if 'jumps' not in data:
            data['jumps'] = []
        data['jumps'] = jumps

        saveProjectJsonById(projId, data)
        return True

# Searches through the project folder and registers found projects into projects.json
def discoverProjects():
    projects = []
    projectId = 0

    for root, subdirectories, files in os.walk(projectsFolder):
        if 'project.json' in os.listdir(root):
            with open(os.path.join(root, 'project.json'), "r") as f: 
                data = json.load(f)
                if 'projectName' in data:
                    projects.append({'name': data['projectName'], 'path': root, 'id': projectId})
                    projectId+=1
                            
    with open(os.path.join(projectsFolder, 'projects.json'), "r+") as f: 
        data = json.load(f)
        if 'projects' not in data:
            data['projects'] = []
        data['projects'] = projects
        f.seek(0)
        f.truncate()
        json.dump(data, f)
    

# Returns projects.json contents
def getProjects():
    with open(os.path.join(projectsFolder, 'projects.json'), "r") as f: 
        return json.load(f)

# Fetches scene object by projectId and sceneId
def getSceneById(projectId, sceneId):
    projectData = getProjectJsonById(projectId)
    data = projectData['scenes'][int(sceneId)]
    if data:
        return data
    return False

def getResourceListById(projectId):
    projectData = getProjectJsonById(projectId)
    if 'resources' not in projectData.keys():
        print('resource list not in project.json for project: ' + projectId)
        return False
    data = projectData['resources']
    return data

def writeScriptByProjectId(projectId):
    project = getProjectJsonById(projectId)
    if not project:
        print('Failed to find project with id of ' + projectId)
        return False
    projectInfo = getProjects()['projects'][projectId]
    if not projectInfo:
        print('Failed to write project: ' + project['projectName'])
        return False

    output = ''
    # Resources
    output += writeResources(project['resources'], projectInfo)
    # Scenes
    for scene in project['scenes']:
        output += writeScene(scene)

    # Write file
    if projectInfo:
        try:
            with open(os.path.join(projectInfo['path'], "game/script.rpy"), 'w') as f:
                f.write(output)
                print("Wrote script to: "+ projectInfo['path'] + "/script.rpy")
                return True
        except FileNotFoundError:
            print('The file does not exist.\n')
    print('Failed to write project: ' + project['projectName'])
    return False

def writeScene(scene):
    s = ''
    s += 'label ' + scene['name'] + ':\n'
    for l in scene['lines']:
        if l['type'] == 'text':
            # text
            if l['character'] != '':
                s += "    \"%s\" \"%s\"\n"%(l["character"],l['text'].replace('\"','\\\"'))
            else:
                s += "    \"%s\"\n"%(l['text'].replace('\"','\\\"'))
        elif l['type'] == 'show':
            s += "    show %s\n"%(l['text'])
        elif l['type'] == 'jump':
            # text
            s += "    jump %s\n"%(l['text'])
        elif l['type'] == 'scene':
            # text
            s += "    scene %s\n"%(l['text'])
        elif l['type'] == 'sfx':
            # text
            s += "    play sound %s\n"%(l['text'])
        elif l['type'] == 'music':
            # text
            s += "    play music %s\n"%(l['text'])
        elif l['type'] == 'script':
            # text
            print('no script support')
        else:
            print('unknown type on line with id: '+l['uniqueId']+' on scene: '+scene['name'])
    return s

def writeResources(resources, projectInfo):
    s = "" 
    if 'character' in resources:
        for character in resources['character'].values():
            s += 'image %s = \"%s\"\n'%(character['name'],character['fileName'])
            file = shutil.copy(character['fileDir'],os.path.join(projectInfo['path'], 'game', 'images', character['fileName']))
    if 'background' in resources:
        for background in resources['background'].values():
            s += 'image %s = \"%s\"\n'%(background['name'],background['fileName'])
            file = shutil.copy(background['fileDir'],os.path.join(projectInfo['path'], 'game', 'images', background['fileName']))
    if 'sfx' in resources:
        for sfx in resources['sfx'].values():
            s += 'define audio.%s = \"%s\"\n'%(sfx['name'],sfx['fileName'])
            file = shutil.copy(sfx['fileDir'],os.path.join(projectInfo['path'], 'game', 'audio', sfx['fileName']))
    if 'music' in resources:
        for music in resources['music'].values():
            s += 'define audio.%s = \"%s\"\n'%(music['name'],music['fileName'])
            file = shutil.copy(music['fileDir'],os.path.join(projectInfo['path'], 'game', 'audio', music['fileName']))
    return s

def createProject(name):
    if not os.path.exists(os.path.join(projectsFolder,name)):
        shutil.copytree(baseProjectFolder,os.path.join(projectsFolder,name))
        if 'project.json' in os.listdir(os.path.join(projectsFolder,name)):
            with open(os.path.join(os.path.join(projectsFolder,name), 'project.json'), "r+") as f: 
                data = json.load(f)
                data['projectName'] = name
                f.seek(0)
                f.truncate()
                json.dump(data, f)
        return True
    print("Project with that name already exists")
    return False
        
def deleteProject(name):
    if os.path.exists(os.path.join(projectsFolder,name)):
        shutil.rmtree(os.path.join(projectsFolder,name))
        return True
    print("Failed to delete project")
    return False