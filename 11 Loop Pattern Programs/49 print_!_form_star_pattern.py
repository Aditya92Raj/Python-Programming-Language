#Write a program to print ! form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if ((j==1 and i>=1 and i<a-1) or (i==a and j==1)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
