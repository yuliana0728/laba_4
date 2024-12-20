class Employee :
  __name = None

  def __init__(self,name):
    self.__name = name

  def getName(self):
    return self.__name
employees = [
	 Employee('john'),
	 Employee('eric'),
	 Employee('kyle'),
] 
for employee in employees:
	print(employee.getName())
