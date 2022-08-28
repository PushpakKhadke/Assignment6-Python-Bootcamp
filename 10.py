# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

Number1=int(input("Enter 1st Number: "))
Number2=int(input("Enter 2nd Number: "))
Number3=int(input("Enter 3rd Number: "))
if Number1>=Number2 and Number1>=Number3:
    print("Greater Number is ",Number1)
elif Number2>Number1 and Number2>Number3:
    print("Greater Number  is ",Number2)
else:
    print("Greater Number is ",Number3)


"""
2nd Way!

Number1=int(input("Enter 1st Number: "))
Number2=int(input("Enter 2nd Number: "))
Number3=int(input("Enter 3rd Number: "))
print((Number1 if Number1>Number3 else Number3) if Number1>Number2 else(Number2 if Number2>Number3 else Number3))
"""



























#
# a ,b, c = 20, 30, 10
#
# if a > b:
#     if a > c:
#         print("%d is greter" %(a))
#     else:
#         print("%d is greter" %(c))
# elif b > c:
#     print("%d is greter" %(b))
# else:
#     print(("%d is greter" %(c)))
