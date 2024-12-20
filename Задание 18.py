class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def getName(self):
        return self.__name
    def getSal(self):
        return self.__salary + '$'
    def getAge(self):
        return self.__age
    def setName(self,name):
		          self.__name = name 
	def setSal(self,salary):
		         self.__salary = salary
	def setAge(self,salary):
	  if (len(age) < 0 and (len(age) > 120:
	             self.__age = age
	  raise Exception('age is incorrect')
