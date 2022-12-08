# --------------If Else--------------------
# n = 10
# if (n<=0):
#     print("the value is less than zero")
# elif (n==10):
#     print("value is  equal to 10")
# else:
#     print("n is greater than 10")



# product_1 = float(input("quantity of first product: "))
# product_2 = float(input("quantity of second product: "))
# product_3 = float(input("quantity of third product: "))
# if((product_1<=0) or (product_2<=0) or (product_3<=0)):
#     print("please enter the correct value")
# else:
#     print("The amount that you need to pay is: ")
#     total = product_1*200 + product_2*300 + product_3*400
#     print(total)



#-------------(loops concept) List------------
#students = ['rahul','sai','krishna','radha','lavanya','deepu','loukya','devanshika','ramu']
# for s in students:
#     print("the student name is: ",s)

# students = ['rahul','sai','krishna','radha','lavanya','deepu','loukya','devanshika','ramu']
# print("The student names are: ")
# for s in students:
#     print(s)



# l = [1, 2, 3.2, 410, 2.5,'sai','krishna',True]
# print(l)
# print(l[0])
#print(l[1:4]) #include one and exclude 3
# l1 = ['ravi','chandu']
# print(l1+l)


#----------------Tuple------------------
# t = (1,2,3,4.2,53.2,'aditya','deepu',False)
# print(t[0])
# print(t[1:4])
# print(t[2:])


#-----------dictionary(it has a keys and values)-----------
# details = {'ram' : 90, 'sai' : 95, 'krishna' : 96, 'deepu' : 97}
# details[4] = "testing"
# print(details)
# print(details.values())
# print(details.keys())
# print(details[4])


# dict = {
#     "collage" : "Aditya",
#     "Religion" : "Hindu",
#     "stream" : "EEE"
# }
# for info in dict:
#     print(info)
# for info1 in dict:
#     print(dict[info1])


# collage = {}
name = input("enter collage name: ")
rollnum = input("enter Roll Num:")
# #collage[name]=rollnum
# #print(collage)
collage1 = {name:rollnum}
print(collage1)