#Write a program to input number from user and print zigzag pyramid star pattern.
space=0
a=int(input("Enter a number:"))
for x in range(1,a+1,2):
    print(" "*space+"*"*x)
    space+=1
