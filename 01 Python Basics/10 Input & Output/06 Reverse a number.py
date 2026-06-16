#Write a program to input number from user and reverse their number?
a=int(input("Enter your number:"))
s=a
c=a%10
a//=10
b=a%10
a//=10
print(f"reverse of {s}=",c*100+b*10+a)
