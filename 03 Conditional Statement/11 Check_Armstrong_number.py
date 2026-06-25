#Write a program to input number from user and check whether given number is Armstrong or not.
a=int(input("Enter a three digit number:"))
x=a
c=a%10
a//=10
b=a%10
a//=10
if x==a**3+b**3+c**3:
    print(f"{x} is Armstrong")
else:
    print(f"{x} is not Armstrong")
