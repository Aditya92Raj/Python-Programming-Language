#Write a program to input number from user and check whether given number is palindrome or not.
s=0
a=int(input("Enter a number:"))
z=a
while(a>0):
    r=a%10
    a//=10
    s=s*10+r
if z==s:
    print("palindrome")
else:
    print("not palindrome")
