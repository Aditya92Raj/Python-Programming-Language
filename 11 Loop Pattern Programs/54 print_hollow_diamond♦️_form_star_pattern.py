#Write a program to print hollow diamond form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (j==a+a//2+1-i or j+a//2==i or i+j==a//2+2 or i+a//2==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()
