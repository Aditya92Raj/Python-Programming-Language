#Write a program to print 3 form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((i==1 and j!=1) or (j==a+1-i and j>=a//2+1) or (i==a//2+1 and j>a//2+1 and j<a) or (i==a and j!=a and j!=1) or (j==a and i>a//2+1 and i<a)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
