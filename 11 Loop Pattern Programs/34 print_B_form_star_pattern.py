#Write a program to print B form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (j==1 or (i==1 and j!=a) or (i==a//2+1 and j!=a) or (i==a and j!=a) or (j==a and i!=1 and i!=a//2+1 and i!=a)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
