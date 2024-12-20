class Employee :
  name = None
  position = None
  department = None

  def __init__(self, name, position, department):
    self.name = name
    self.position = position
    self.department = department
name = Name('john')
position = Position('accountant')
employee1 = Employee(name, position, 'accounting')
print(employee1.name.position)
