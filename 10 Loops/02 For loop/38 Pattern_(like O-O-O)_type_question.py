#Write a program to input number from user and print(like O-O-O) according to given number.
a=int(input("Enter a number:"))
for x in range(1,a):
    print("O-",end="")
print("O")
