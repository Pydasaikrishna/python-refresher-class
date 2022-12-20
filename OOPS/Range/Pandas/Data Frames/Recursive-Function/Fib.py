#Recursion means function calls itself

def Rect_fib(n):
    if (n<=1):
        return n
    else:
        return(Rect_fib(n-1) + Rect_fib(n-2))

Entries = int(input("Enter a number: "))
if (Entries<=0):
    print("Invalid Entry")
else:
    print("Fibbino series: ")
    for i in range(Entries):
        print(Rect_fib(i))

