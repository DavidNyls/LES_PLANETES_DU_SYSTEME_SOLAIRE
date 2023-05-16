import json

class Cookie :

    def __init__(self, name):
        self.name = name

    def create(self):
        with open(self.name, 'w') as my_file:
            print (f"cookie {self.name}: a été créé")

    def read(self):
        with open(self.name, "r") as my_file:
            return json.load(my_file)

    def write(self, dict):
        with open(self.name, 'w') as my_file:
            json.dump(dict, my_file)


    def update(self, data):
        c = self.read()
        keys = list(c.keys())

        for key in keys :
            c[key] = data[key]

        self.write(c)

    def clean(self):
        c = self.read()
        keys = list(c.keys())

        for key in keys :
            c[key] = None

        self.write(c)

    def drop(self):
        self.write({})