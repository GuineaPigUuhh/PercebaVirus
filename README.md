## Roblox virus gift card generator
it's an executable virus that passes itself off as a roblox gift card generator.

## Requirements
run this code to install the requirements:
```cmd
pip install -r requirements.txt
```

## Customizing
to customize look at the config file **(res/data/config.json)**
```json
{
    "files_range": 100,
    "file": {
        "url": "",
        "output_name": "IDK"
    },
    "chars": [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"
    ]
}
```
1. **files_range**: how many times will you create the files on your desktop.
2. **file**: configuration of the files that will be created.
    - **url**: the image url
    - **output_name**: the names of the created files.
3. **chars**: features that appeared in the generated code.