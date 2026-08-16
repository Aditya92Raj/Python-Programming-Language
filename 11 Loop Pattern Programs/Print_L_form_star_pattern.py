#Write a program to input number from user and print L form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if (x==a or y==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
