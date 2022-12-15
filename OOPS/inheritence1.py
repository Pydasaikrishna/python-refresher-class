class Person(object):

    def __init__(self,name,id):  #Parameterized constructor
        self.name = name
        self.id = id

    def display(self):
        print(self.name,self.id)

Emp = Person("Aditya college of engg",1001)
Emp.display()

class Sai(Person):

    def Print(self):
        print("Emp class called")

EmpDetails = Sai("Prabhas",1002)
EmpDetails.display()
EmpDetails.Print()




