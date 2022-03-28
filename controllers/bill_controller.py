class BillController(object):
    def __init__(self, billService) -> None:
        self.billService = billService
    
    def addBill(self, id, groupId, amount, contri, paid):
        self.billService.addBill(id, groupId, amount, contri, paid)
    
    def getUserBalance(self, userId):
        # balance = Sum(paid.get(userId) for each bill in which userId paid) - Sum(contri.get(userId) 
        # for each bill in which userId had to contribute)
        balance = 0
        for billId in self.billService.billDetails:
            bill = self.billService.billDetails[billId]
            
            if userId in bill.getPaid():
                balance += bill.getPaid()[userId]
            if userId in bill.getContri():
                balance -= bill.getContri()[userId]
        
        return balance