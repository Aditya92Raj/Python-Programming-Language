#Write a program to input number from user and print P form star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( y==1 or (x==1 and y!=a) or (y==a and x>1 and x<a//2+1) or (x==a//2+1 and y!=a)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
