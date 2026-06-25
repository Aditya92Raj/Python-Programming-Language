#Write a program to input number from user and check whether given number is palindrome or not.
a=int(input("Enter a three digit number:"))
x=a
r=a%10
a//=100
if r==a:
    print(f"{x} is palindrome")
else:
    print(f"{x} is not palindrome")
