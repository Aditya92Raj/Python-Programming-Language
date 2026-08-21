#Write a program to print d form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (j==a or (i==a//2+1 and j!=1) or (i==a and j!=1) or (j==1 and i>a//2+1 and i<a)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
