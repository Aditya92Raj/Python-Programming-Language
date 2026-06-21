#Write a program to input exam percentage and check pass or fail. if pass, print Grade A, B, C or D.
m=int(input("Enter your Marks:"))
if m>=0 and m<=100:
    if m<30:
        print("Fail")
    elif m<50:
        print("Grade-D")
    elif m<70:
        print("Grade-C")
    elif m<90:
        print("Grade-B")
    else:
        print("Grade-A")
else:
    print("Invalid Marks")
