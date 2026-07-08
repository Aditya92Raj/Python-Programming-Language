#Write a program to input number from user and print hollow inverted full pyramid form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( x==1 or (y==x and y<=a//2) or (y==a+1-x and y>=a//2+1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
