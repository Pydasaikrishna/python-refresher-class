# l=[10,20,30,40,50,60,120]
# mx = max(l[0],l[1])
# secondmx = min(l[0],l[1])
# n = len(l)
# for i in range(2,n):
#     if (l[i]>mx):
#         secondmx = mx
#         mx = l(i)
#     elif(l[i]>secondmx and /n ):





l=[]
user_input = int(input("Enter the number of entries: "))
for i in range(1,user_input+1):
    entries = int(input("Enter the numbers: "))
    l.append(entries)

l.sort()
print(l)
print("The second largest number is ",l[-2])