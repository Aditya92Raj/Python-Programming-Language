#Write a program to print 1 form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if(j==a or (j==a+1-i and i<a//2+1)):
            print("*",end="")
        else:
            print(" ", end="")
    print()
