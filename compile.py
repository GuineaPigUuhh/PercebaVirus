import os
import shutil
import backend.paths as paths
from os.path import join, exists
from backend.config import get

def recompile(config: any):
    if not exists(config["output_folder"]):
        os.makedirs(config["output_folder"])

    os.chdir(config["output_folder"])
    for i in config["additional_files"]:
        copyfrom = join(paths.abspath(), "..", i)
        copyto = join(paths.abspath("dist"), i)

        try: shutil.copytree(copyfrom, copyto)
        except Exception as e: shutil.copyfile(copyfrom, copyto)

    # PyInstaller starts compile
    icon = join(paths.abspath(), "..", config["icon"])
    main = join(paths.abspath(), "..", config["main"])
    os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{icon}"  "{main}"')

recompile(get("compiler"))