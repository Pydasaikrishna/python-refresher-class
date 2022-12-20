num = int(input("Enter a Number: "))
flag = False
if(num>=1):
    for i in range(2,num):
        if(num%i == 0):
            flag = True
            break


if(flag):
    print(num,"it is not a Prime Number!!!!")
else:
    print(num,"It is a Prime Number")