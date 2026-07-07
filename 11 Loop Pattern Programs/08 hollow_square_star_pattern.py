#Write a program to input number from user and print hollow square star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if (x==1 or y==1 or x==a or y==a):
            print("*",end="")
        else:
            print(" ",end="")
    print()
