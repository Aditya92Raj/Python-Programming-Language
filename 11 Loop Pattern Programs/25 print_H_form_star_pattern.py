#Write a program to input number from user and print H form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( x==a/2+1 or y==1 or y==a):
            print("*",end="")
        else:
            print(" ",end="")
    print()
