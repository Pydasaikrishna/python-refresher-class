class Person(object):

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

emp = Person("Krishna")
print(emp.getName(),emp.isEmployee())

emp1 = Employee("Sachin")
print(emp1.getName(),emp1.isEmployee())