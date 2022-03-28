class User(object):
    def __init__(self, id=None, name=None) -> None:
        self.id = id
        self.name = name
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.id = name
    
    def getName(self):
        return self.name
    
