#Write a program to input number from user and print hollow right half pyramid star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( y==a or x==a or y==a+1-x):
            print("*",end="")
        else:
            print(" ",end="")
    print()
