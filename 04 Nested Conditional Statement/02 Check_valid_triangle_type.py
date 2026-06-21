#Write a program to input angle (form of number) from user and check given triangle (equilateral, isosceles and scalene) or not according to given angles.
a=int(input("Enter your first angle:"))
b=int(input("Enter your second angle:"))
c=int(input("Enter your third angle:"))
if a+b+c==180:
    if a==b and b==c:
        print("Equilateral triangle")
    elif a==b or b==c or c==a:
        print("Issosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
