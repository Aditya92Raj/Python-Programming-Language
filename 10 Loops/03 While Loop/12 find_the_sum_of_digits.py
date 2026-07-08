#Write a program to input number from user and find the sum of digits.
s=0
a=int(input("Enter a number:"))
while(a>0):
    r=a%10
    s+=r
    a//=10
print("Sum of digits=",s)
