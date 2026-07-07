#Write a program to input number from user and print N form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( y==1 or y==a or y==x):
            print("*",end="")
        else:
            print(" ",end="")
    print()
