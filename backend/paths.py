from os import path as p
import os

def res(path):
    return p.join("res", path)

def img(path, ext = "png"):
    return res(p.join("img", f'{path}.{ext}'))

def data(path):
    return res(p.join("data", f'{path}'))

def json(path):
    return data(f'{path}.json')

# GLOBAL

def abspath(path=""):
    return p.abspath(path)

def userprofile(path):
    profile = "USERPROFILE"
    return p.join(os.environ[profile], path)

def desktop(path):
    return userprofile(p.join("Desktop", path))