class Generator:
    code = ""
    chars = []

    def __init__(self):
        import yaml
        import backend.paths as paths

        self.chars = yaml.safe_load(open(paths.yaml("chars")))["chars"]

    def generate(self):
        import random
        self.code = ""
        for i in range(random.randint(10, 20)):
            self.code += random.choice(self.chars)  