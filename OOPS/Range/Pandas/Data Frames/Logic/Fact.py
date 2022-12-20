num = int(input("Enter a number: "))
fact = 1       #global variable
if(num<0):
    print("Negative numbers are not accepted!!!")
elif(num == 0):
    print("The factorial of Zero is one")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("The factorial of ",num,"is",fact)