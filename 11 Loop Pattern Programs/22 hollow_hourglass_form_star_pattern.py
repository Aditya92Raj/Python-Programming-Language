#Write a program to input number from user and print hollow hourglass star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if (x==1 or x==a or x==y or y==a+1-x):
            print("*",end="")
        else:
            print(" ",end="")
    print()
