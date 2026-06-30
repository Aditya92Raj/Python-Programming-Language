#Write a program to print the multiplication table of a given number.
n=int(input("Enter a number:"))
for x in range(1,11):
    print(f"{n}*{x}=",n*x)
