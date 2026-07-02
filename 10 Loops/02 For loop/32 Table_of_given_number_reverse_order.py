#Write a program to print the table of given number in reverse order.
n=int(input("Enter a number:"))
for x in range(10,0,-1):
    print(f"{n}*{x}=",n*x)
