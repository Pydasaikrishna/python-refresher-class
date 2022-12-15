# numbers = [2,4,5,7,9,10,13,15,17,20]
# for i in numbers:
#     print("current number",i)
#     if i > 10:
#         continue
#     square = i*i
#     print("square of the current number ",square)


#------method-1-------------
# student1 = int(input("Enter student1 marks: "))
# student2 = int(input("Enter student2 marks: "))
# student3 = int(input("Enter student3 marks: "))
# student4 = int(input("Enter student4 marks: "))
# student5 = int(input("Enter student5 marks: "))
# marks = [student1,student2,student3,student4,student5]
# for i in marks:

#     if(i<=40):
#         continue
#     print("marks: ",i)



#-----------method-2-----------
# num = [int(input("Enter student Marks: "))for i in range(5)]
# for i in num:

#     if(i<=40):
#         continue
#     print("marks: ",i)



#------------method-3------------

for i in range(5):
    n = int(input("Enter marks: "))
    if n == 40:
        continue
    print(n)