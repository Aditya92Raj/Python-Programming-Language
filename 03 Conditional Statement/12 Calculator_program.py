#Calculator (+,-,*,/,**) in python:-
a=int(input("Enter your first number:"))
b=input("Enter your operator:")
c=int(input("Enter your second number:"))
if b=='+':
    print(a+c)
elif b=='-':
    print(a-c)
elif b=='*':
    print(a*c)
elif b=='/':
    print(a/c)
elif b=='**':
    print(a**c)
else:
    print("error...")
