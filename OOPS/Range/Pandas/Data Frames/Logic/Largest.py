n1 = int(input("Enter the Number: "))
n2 = int(input("Enter the Number: "))
n3 = int(input("Enter the Number: "))

if(n1 >= n2) and (n1>=n3):
    largest = n1
elif(n2 >= n3) and (n2 >= n3):
    largest = n2
else:
    largest = n3

print("Largest Number is",largest)