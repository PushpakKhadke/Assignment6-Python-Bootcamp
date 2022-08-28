# 9. Write a python script to check whether a given year is a leap year or not.

Year=int(input("Enter The Year: "))
print("Leap Year" if Year%4==0 and Year%100!=0 or Year%400==0 else "Not Leap year")
print()

