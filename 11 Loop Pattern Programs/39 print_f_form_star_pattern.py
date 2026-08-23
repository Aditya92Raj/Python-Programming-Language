#Write a program to print f form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if((j==a//2+1 and i!=1) or (i==1 and j>a//2+1) or i==a//2+1):
            print("*",end="")
        else:
            print(" ", end="")
    print()
