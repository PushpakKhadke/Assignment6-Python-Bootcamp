# 2. Write a python script to check whether a given number is divisible by 5 or not

Number=int(input("Enter The Number: "))
if Number%5==0:
    print("Divisible")
else:
    print("Not-Divisible")
print()




"""
2nd Way!

print("Divisible" if int(input("Enter The Number: "))%5==0 else"Not-Divisible")
"""
