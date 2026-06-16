#Write a program to input number from user and gives output at sum their number?
a=int(input("Enter your number:"))
c=a%10
a//=10
b=a%10
a//=10
print("sum of digits=",a+b+c)
