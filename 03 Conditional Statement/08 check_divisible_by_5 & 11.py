#Write a program to check whether a number is divisible by both 5 and 11.
a=int(input("Enter a number:"))
if a%5==0 and a%11==0:
    print("Divisible by 5 and 11")
else:
    print("Not Divisible")
