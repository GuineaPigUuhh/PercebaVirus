import json
import backend.paths as paths

content = json.load(open(paths.json("config")))

def get(name: str):
    global content
    return content[name]