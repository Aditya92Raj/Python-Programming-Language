#Write a program to find the average of numbers from 1 to n.
s=0
n=int(input("Enter a number:"))
for x in range(1,n+1):
    s+=x
print(f"Average of {n} natural number=",s/n)
