#Write a program to print 7 form star pattern.
a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==1 or j==a+1-i):
            print("*",end="")
        else:
            print(" ", end="")
    print()
