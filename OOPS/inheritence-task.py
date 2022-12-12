# Create a class - Employee for two employees with some objects
# Fetch name,age and salary and display in the screen


# class Employee():

#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def display(self):
#         print(self.name,self.age,self.salary)

# Deepu = Employee("Raghava",25,3000)
# Deepu.display()

# class Emp(Employee):

#     def Print(self):
#         print("okay")

# empDetails = Emp("krishna",20,80000)
# empDetails.display()


# ------------------------------ Task-1 -----------------------
# class Employee:  #creating the class

#     company = "Aditya college"      #company is class attribute

#     def __init__(self,name,age,salary):    #default constructor
# #name age and salary are attributes or variables
#         self.name = name
#         self.age = age
#         self.salary = salary

# #creating objects

# emp1 = Employee("Krishna",20,80000)
# emp2 = Employee("Sai",18,100000)

# #print(f"{}) is the formatted string
# print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company}")
# print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
# print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")



# ----------------------------- Task-2 -------------------------
#Create a class - student.use the method concept
#to fetch student name and marks for them

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def getDetails(self):
        print(f"hii my name is {self.name}, i recieved {self.marks} marks.")

    def getDetails1(self):
        print(f"hii my name is {self.name},i received {self.marks} marks.")

stud1 = Student("krishna",95)
stud2 = Student("deepu",100)

stud1.getDetails()
stud2.getDetails1()