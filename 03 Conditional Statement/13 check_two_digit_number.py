#Write a program to input number from user and check whether given number is two digit or not.
a=int(input("Enter a number:"))
if a>=10 and a<=99:
    print("Two-digit number")
else:
    print("Not a two-digit number")
