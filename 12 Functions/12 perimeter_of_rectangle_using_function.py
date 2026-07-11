#Write a function to find the perimeter of a rectangle.
def prmtr(l,b):
    return 2*(l+b)
l=int(input("Enter a length:"))
b=int(input("Enter a breadth:"))
s=prmtr(l,b)
print("perimeter of rectangle=",s)
