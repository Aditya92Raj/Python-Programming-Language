#Write a program to print # form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (i==a//4+1 or j==a//4+1 or i==a*3//4+1 or j==3*a//4+1):
            print("*",end="")
        else:
            print(" ", end="")
    print()
