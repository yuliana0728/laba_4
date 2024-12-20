class Emloyee():
    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name + self.salary)
empoloyee = Emloyee('john', 215000')
emloyee.show()
