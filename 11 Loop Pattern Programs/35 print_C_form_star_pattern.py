#Write a program to print C form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((j==1 and i!=1 and i!=a) or (i==1 and j!=1 and j!=a) or (i==a and j!=1 and j!=a) or (i>1 and i<=a//4+1 and j==a) or (i>=3*a//4+1 and i<a and j==a)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
