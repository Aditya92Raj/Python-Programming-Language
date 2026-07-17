#Write a program to input number from user and check whether given number is three digit or not.
a=int(input("Enter a number:"))
if a>=100 and a<=999:
    print("Three-digit number")
else:
    print("Not a three-digit number")
