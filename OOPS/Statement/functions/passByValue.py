def ChangeNumber(mylist):
    mylist.append([1,2,3,4,5,6])
    print("Values inside the function ",mylist)
    return

mylist = [40,50,60,70]

print("Values outside the function ",mylist)
ChangeNumber(mylist)
# print("Values outside the function ",mylist)