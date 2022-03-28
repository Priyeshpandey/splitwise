class Group(object):
    def __init__(self, id=None, name=None, members=None) -> None:
        self.id = id
        self.name = name
        self.members = []
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.id = name
    
    def getName(self):
        return self.name
    
    def setMembers(self, memberList):
        self.members = memberList
    
    def getMembers(self):
        return self.members

