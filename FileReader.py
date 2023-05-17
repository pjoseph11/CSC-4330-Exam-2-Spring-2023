class Read:
    #method initializes variables
    def __init__(self, path):
        self.path = path
        self.contents = ''
    #method stores contents of file as string
    def readFile(self):
        with open(self.path, 'r') as file:
            self.contents = file.read()