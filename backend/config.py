import json
import backend.paths as paths

content = None

def get(name: str):
    global content
    if content == None: content = json.load(open(paths.json("config")))
    return content[name]