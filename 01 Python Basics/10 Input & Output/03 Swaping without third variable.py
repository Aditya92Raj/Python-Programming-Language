#Input in python
#Swapping numbers without help of third variable. 
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
print("Before swapping")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("After swapping")
print("a=",a)
print("b=",b)
