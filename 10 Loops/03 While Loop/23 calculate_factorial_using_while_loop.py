#Write a program to calculate factorial using a for loop.
s=1
a=1
n=int(input("Enter a number:"))
while(a<=n):
    s*=a
    a+=1
print(f"{5}!=",s)
