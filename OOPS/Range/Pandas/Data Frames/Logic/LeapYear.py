year = int(input("Enter Leap Year: "))
if((year%400==0) and (year%100==0)):
    print("{0} is the Leap Year".format(year))
elif((year%4==0) and (year%100!=0)):
    print("{0} is the Leap Year".format(year))
else:
    print("{0} is not a leap year".format(year))