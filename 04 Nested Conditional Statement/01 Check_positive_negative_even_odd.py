#Write a program to input number from user and check given number is positive even, positive odd, negative even, negative odd.
a=int(input("Enter a number:"))
if a==0:
    print("Zero")
elif a>0:
    if a%2==0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if a%2==0:
        print("Negative Even")
    else:
        print("Negative Odd")
