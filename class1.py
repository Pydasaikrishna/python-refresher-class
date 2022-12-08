# batcount = int(input("no.of bats sold: "))
# wicketcount = int(input("no.of wickets sold: "))
# shoescount = int(input("no.of shoes sold: "))
# totalcount = batcount*500 + wicketcount*200 + shoescount*400
# print("user need to pay",totalcount)


# batcount = int(input("no.of bats sold: "))
# wicketcount = int(input("no.of wickets sold: "))
# if(batcount<=0 or wicketcount<=0):
#    print("Enter a positive number")


# batcount = int(input("no.of bats sold: "))
# wicketcount = int(input("no.of wickets sold: "))
# if(batcount<=0 and wicketcount<=0):
#    print("Enter a positive number")



product_1 = int(input("quantity of first product: "))
product_2 = int(input("quantity of second product: "))
product_3 = int(input("quantity of third product: "))
product_4 = int(input("quantity of fourth product: "))
product_5 = int(input("quantity of fifty product: "))

#using List
l = [product_1,product_2,product_3,product_4,product_5]

#using For loop
# for i in l:
#    print(i)

#using If_Else statement
if((product_1<=0) or (product_2<=0) or (product_3<=0) or (product_4<=0) or (product_5<=0)):
    print("please enter the correct value")
else:
    print("The product quantity with price: ")
    total = product_1*200 + product_2*300 + product_3*400 + product_4*100 + product_5*200
    entries = {product_1 : 200,product_2 : 300, product_3 : 400, product_4 : 100, product_5 : 200}
    #i=product_1... etc  and p=price..,
    for i,p in entries.items():
      print(i,p)
    print("The amount that you need to pay is: ")
    print(total)

