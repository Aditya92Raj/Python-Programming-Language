#Write a program to print U form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((j==a and i!=1 and i!=a) or (j==1 and i!=a and i!=1) or (i==a and j!=1 and j!=a)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
