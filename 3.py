# 3. Write a python script to check whether a given number is even or odd

Number=int(input("Enter a Number: "))
if Number%2==0:
    print("Even Number")
else:
    print("Odd Number")
print()



"""
2nd Way!

print("Even Number" if int(input("Enter a Number: "))%2==0 else"Odd Number")
"""