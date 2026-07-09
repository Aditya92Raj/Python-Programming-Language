#Write a program to input number from user and find the sum of even numbers from 1 to n.
a=2
s=0
n=int(input("Enter a number:"))
while(a<=n):
    s+=a
    a+=2
print(s)
