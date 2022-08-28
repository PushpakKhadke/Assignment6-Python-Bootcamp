# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

Number1=int(input("Enter The Number:"))
Number2=int(input("Enter The Number:"))
if Number1>Number2:
    print(Number1,"Is Greater Than",Number2)
elif Number1==Number2:
    print("Number Are Same")
else:
    print(Number2,"Is Greater Than",Number1)
print()


