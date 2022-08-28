# 11. Write a python script to take the month value in numeric format and display the number of days in it.

Month = int(input("Enter a Month Number: "))
if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
    print("31 Days Month")
elif Month==2:
    print("28 Or 29 Days  Month")
else:
    print("30 Days  Month")
print()



