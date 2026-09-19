#Write a program to print → form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (i==a//2+1 or i+a//2==j or j==a+a//2+1-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
