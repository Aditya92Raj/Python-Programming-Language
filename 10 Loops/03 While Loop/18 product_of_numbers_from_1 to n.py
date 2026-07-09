#Write a program to input number from user and find the product of numbers from 1 to n
a=1
s=1
n=int(input("Enter a number:"))
while(a<=n):
    s*=a
    a+=1
print(s)
