#Write a program to find the smallest of four numbers.
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
if a<b and a<c and a<d:
    print(f"{a} is smallest")
elif b<c and b<d:
    print(f"{b} is Smallest")
elif c<d:
    print(f"{c} is Smallest")
else:
    print(f"{d} is Smallest")
