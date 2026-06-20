#Write a program to check whether three angles form a valid triangle.
a=int(input("Enter your first angle:"))
b=int(input("Enter your second angle:"))
c=int(input("Enter your third angle:"))
if a+b+c==180:
    print("A valid triangle")
else:
    print("Not a valid Triangle")
