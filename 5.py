# 5. Write a python script to print two given words in dictionary order

First_Word=(input("Enter The Word: "))
Second_Word=(input("Enter The Word: "))
print((Second_Word,First_Word) if First_Word>Second_Word else  (First_Word,Second_Word))
