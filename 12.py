# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

Complex=complex(input("Enter a complex number: "))
if Complex.real > Complex.imag:
    print("%d is Greter" %(Complex.real))
elif Complex.real < Complex.imag:
    print("%d is Greter" %(Complex.imag))
else:
    print("Both are equal")
print()