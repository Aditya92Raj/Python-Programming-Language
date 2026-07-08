#Write a program to input number from user and count the digits in a number.
s=0
a=int(input("Enter a number:"))
while(a>0):
    r=a%10
    s+=1
    a//=10
print(s)
