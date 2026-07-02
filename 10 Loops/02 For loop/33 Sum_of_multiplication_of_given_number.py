#Write a program to find the sum of a multiplication table.
n=int(input("Enter a number:"))
p=0
for x in range(1,11):
    print(f"{n}*{x}=",n*x)
    p+=n*x
print("Sum of multiplication table=",p)
