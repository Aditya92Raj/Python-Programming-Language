#Write a program to print G form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((j==1 and i!=1 and i!=a) or (i==1 and j!=1) or (i==a and j!=1) or (j==a and i>=a//2+1 and i!=a) or (i==a//2+1 and j>=a//2+1)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
