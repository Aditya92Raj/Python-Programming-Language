#Write a program to input number from user and reverse the digits of a number.
s=0
a=int(input("Enter a number:"))
while(a>0):
    r=a%10
    a//=10
    s=s*10+r
print("Number in reverse order=",s)
