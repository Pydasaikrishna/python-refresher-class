Entries = int(input("Enter how many Entries u want: "))
n1,n2 = 0,1
count = 0
if(Entries<=0):
    print("Enter the positive number!!!!")
elif(Entries == 1):
    print("Fibno Series upto",Entries)
    print(n1)
else:
    print("Fibno Series")
    while(count < Entries):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1