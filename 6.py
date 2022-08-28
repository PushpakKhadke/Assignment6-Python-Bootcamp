# 6. Write a python script to check whether a given number is a three digit number or not.

Number=int(input("Enter The Number: "))
if 99<Number<1000:
    print("Three Digit")
else:
    print("Not Three Digit")


"""
2nd Way!

print("Three Digit" if 99<int(input("Enter The Number: "))<1000  else"Not Three Digit")

"""