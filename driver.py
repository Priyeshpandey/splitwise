import sys
import os

from models import bill

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)
print(ROOT_DIR)

from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController
from services.bill_service import BillService
from services.group_service import GroupService
from services.user_service import UserService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user_list = []
user_list.append(userController.addUser("user1", "mohan"))
user_list.append(userController.addUser("user2", "sohan"))
user_list.append(userController.addUser("user3", "rohan"))
user_list.append(userController.addUser("user4", "fohan"))
user_list.append(userController.addUser("user5", "lohan"))
# print(user_list)
group1 = groupController.addGroup("group1", "maniacs", user_list)

# print(group1.getMembers())

paid = {"user1":100,"user2":200,"user3":500,"user4":20,"user5":80}
contri = {"user1":180,"user2":180,"user3":180,"user4":180,"user5":180}

billController.addBill("bill1", "group1", 900, contri=contri,paid=paid)

print(billController.getUserBalance("user1"))
print(billController.getUserBalance("user2"))
print(billController.getUserBalance("user3"))


