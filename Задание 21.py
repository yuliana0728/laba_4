1. True False
2. 
class Student:
  name = None

  def __init__(self,name):
    self.name = name

class Employee:
  name = None

  def __init__(self,name):
    self.name = name


users = [
	 Student('user1'),
	 Employee('user2'),
	 Student('user3'),
	 Employee('user4'),
	 Student('user5'),
	 Employee('user6'),
	 Student('user7'),
]
for user in users:
    print(user)
