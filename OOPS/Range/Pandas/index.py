import pandas as pd
# a=[1,7,2]
# myVar = pd.Series(a, index=["x","y","z"])
# print(myVar)

# a1 = [75,80,90,95]
# y = pd.Series(a1,index=["sai","krishna","deepu","raghava"])
# print(y)



#============Add these content in file using file handling============
studentname = [input("Enter Name: ")for i in range(2)]
marks = [input("Enter Marks: ")for i in range(2)]
Q = open("series.txt","w")
z = pd.Series(marks,index=[studentname])
print(z)
print(z,file=Q)