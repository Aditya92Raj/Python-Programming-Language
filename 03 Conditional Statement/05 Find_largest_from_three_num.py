#Write a program to find the largest of three numbers.
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))
if a>b and a>c:
    print(f"{a} is largest")
elif b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
