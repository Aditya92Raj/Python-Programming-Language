#Write a program to calculate factorial using a for loop.
s=1
n=int(input("Enter a number:"))
for x in range(1,n+1):
    s*=x
print(f"{5}!=",s)
