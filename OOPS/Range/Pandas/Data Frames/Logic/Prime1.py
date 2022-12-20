n = int(input("Enter the Number: "))
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print(n,"It is not a Prime Number!!!!")
            print(i,"Times",n//i,"is",n)
            break
        else:
            print(n,"It is a Prime Number")
else:
    print(n,"Is not a Prime Number!!!!")