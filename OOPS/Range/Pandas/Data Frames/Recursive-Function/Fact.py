# def Rec_fact(n):
#     if (n==0):
#         return 1

#     return n*Rec_fact(n-1)

# n = int(input("Enter a number: "))
# print(Rec_fact(n))



def Sai(x):
    if x == 0:
        return 1

    return x*Sai(x-1)

x=int(input("Enter a number: "))
print(Sai(x))
