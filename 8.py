# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

A=int(input("Enter Value Of A: "))
B=int(input("Enter Value Of B: "))
C=int(input("Enter Value Of C: "))
D = B**2 - 4 * A * C
if D > 0:
    print("Real & Distinct Roots")
elif D == 0:
    print("Real & Equal Roots")
else:
    print("Imaginary Roots")
print()
