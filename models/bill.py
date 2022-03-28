class Bill(object):
    def __init__(self, id=None, groupId=None) -> None:
        self.id = id
        self.groupId = groupId
        self.contri = {}
        self.paid = {}
        self.amount = 0
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setGroupId(self, groupId):
        self.groupId = groupId
    
    def getGroupId(self):
        return self.groupId
    
    def setContri(self, contri):
        self.contri = contri
    
    def getContri(self):
        return self.contri
    
    def setPaid(self, paid):
        self.paid = paid
    
    def getPaid(self):
        return self.paid
    
    def setAmount(self, amount):
        self.amount = amount
    
    def getAmount(self):
        return self.amount
    