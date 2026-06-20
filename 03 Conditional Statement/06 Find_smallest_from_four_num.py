#Write a program to find the smallest of four numbers.
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=int(input("Enter a number:"))
if a<b and a<c and a<d:
    print(f"{a} is smallest")
elif b<c and b<d:
    print(f"{b} is Smallest")
elif c<d:
    print(f"{c} is Smallest")
else:
    print(f"{d} is Smallest")
