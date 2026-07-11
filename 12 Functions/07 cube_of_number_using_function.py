#Write a program to input number from user and print cube of number using function in python.
def cube(a):
    return a*a*a
n=int(input("Enter a number:"))
s=cube(n)
print("cube of number=",s)
