#Write a program to input number from user and find the product of digits.
s=1
a=int(input("Enter a number:"))
while(a>0):
    r=a%10
    s*=r
    a//=10
print("product of digits=",s)
