#Write a program to find the average of numbers from 1 to n.
s=0
a=1
n=int(input("Enter a number:"))
while(a<=n):
    s+=a
    a+=1
print(f"Average of {n} natural number=",s/n)
