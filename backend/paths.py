from os import path as p

def res(path):
    return p.join("res", path)

def img(path, ext = "png"):
    return res(p.join("img", f'{path}.{ext}'))

def yaml(path, ext = "yaml"):
    return res(p.join("data", f'{path}.{ext}'))