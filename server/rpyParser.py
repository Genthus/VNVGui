#rpy parser
import os
import shutil
import json

# Main folder where project directories and projects.json is stored
projectsFolder = "../projects"
# Directory for base project
baseProjectFolder = "./defs/base"

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

# Takes data of new resource file and adds it to project.json
def saveResourceFile(projName, name, type, fileName, fileDir):
    with open(os.path.join(projectsFolder,projName,"project.json"), 'r+') as f:
        data = json.load(f)
        if 'resources' not in data:
            data["resources"] = {}
        if type not in data["resources"]:
            data["resources"][type] = {}

        if name in data["resources"][type]:
            print("data exists")
        else:
            data["resources"][type][name] = {'name': name,'type': type,'fileName': fileName, 'fileDir': fileDir}
        f.seek(0)
        f.truncate()
        json.dump(data, f)
        return True

# Finds jump instructions inside scenes and adds them to a key in the root of project.json
def setJumps(projName):
    with open(os.path.join(projectsFolder,projName,"project.json"), 'r+') as f:
        data = json.load(f)

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

        f.seek(0)
        f.truncate()
        json.dump(data, f)
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
    if data:
        return data
    
    return False

def writeScriptByProjectId(projectId):
    project = getProjectJsonById(projectId)
    if not project:
        print('Failed to find project with id of ' + projectId)
        return False
    projectInfo = getProjects()[projectId]
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
    for l in scene['lines']:
        if l['type'] == 'text':
            # text
            if l['character'] != '':
                s += "\t%s \"%s\"\n"%(l["character"],l['text'])
            else:
                s += "\t\"%s\"\n"%(l['text'])
        elif l['type'] == 'show':
            s += "\tshow %s\n"%(l['text'])
        elif l['type'] == 'jump':
            # text
            s += "\tjump %s\n"%(l['text'])
        elif l['type'] == 'scene':
            # text
            s += "\tscene %s\n"%(l['text'])
        elif l['type'] == 'sfx':
            # text
            s += "\tplay sound %s\n"%(l['text'])
        elif l['type'] == 'music':
            # text
            s += "\tplay music %s\n"%(l['text'])
        elif l['type'] == 'script':
            # text
            print('no script support')
        else:
            print('unknown type on line with id: '+l['uniqueId']+' on scene: '+scene['name'])
    return s

def writeResources(resources, projectInfo):
    s = ''
    for character in resources['character']:
        s += 'image %s = \"%s\"'%(character['name'],character['fileName'])
        file = shutil.copy(character['fileDir'],os.path.join(projectInfo['path'], 'game', 'images', character['fileName']))
    for background in resources['background']:
        s += 'image %s = \"%s\"'%(background['name'],background['fileName'])
        file = shutil.copy(background['fileDir'],os.path.join(projectInfo['path'], 'game', 'images', background['fileName']))
    for sfx in resources['sfx']:
        s += 'define audio.%s = \"%s\"'%(sfx['name'],sfx['fileName'])
        file = shutil.copy(sfx['fileDir'],os.path.join(projectInfo['path'], 'game', 'audio', sfx['fileName']))
    for music in resources['music']:
        s += 'define audio.%s = \"%s\"'%(music['name'],music['fileName'])
        file = shutil.copy(music['fileDir'],os.path.join(projectInfo['path'], 'game', 'audio', music['fileName']))
    return s

def createProject(name):
    if not os.exists(os.path.join(projectsFolder,name)):
        shutil.copytree(baseProjectFolder,os.path.join(projectsFolder,name))
        return True
    print("Project with that name already exists")
    return False
        


##
##
## Anything beyond this point needs to be changed
##
##