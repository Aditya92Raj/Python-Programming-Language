#Write a program to input number from user and print hollow left half pyramid star pattern.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    for y in range(1,a+1):
        if ( y==1 or x==a or x==y):
            print("*",end="")
        else:
            print(" ",end="")
    print()
