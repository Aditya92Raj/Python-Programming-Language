#Write a program to input number from user and print star pattern form of pyramid according to given number.
a=int(input("Enter a number:"))
for x in range(1,a+1):
    print(" "*(a-x)+"* "*x)
