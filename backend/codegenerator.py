import backend.config as config

class Generator:
    code = ""
    chars = []

    def __init__(self):
        self.chars = config.get("chars")

    def generate(self):
        import random
        self.code = ""
        for i in range(random.randint(10, 20)):
            self.code += random.choice(self.chars)  
        return self.code