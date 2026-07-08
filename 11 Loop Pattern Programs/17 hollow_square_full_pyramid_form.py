#Write a program to input number from user and print hollow full pyramid form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( x==a or (x==y and y>=a//2+1) or (y==a+1-x and y<=a//2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
