#Write a program to input number from user and print swastik star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if (y==a//2+1 or x==a//2+1 or (x==1 and y>=a//2+1) or (x==a and y<=a//2+1) or (y==1 and x<=a//2+1) or (y==a and x>=a//2+1)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
