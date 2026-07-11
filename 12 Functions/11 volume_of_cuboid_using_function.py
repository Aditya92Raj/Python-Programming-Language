#Write a function to find the volume of a cuboid.
def volume(l,b,h):
    return l*b*h
l=int(input("Enter a length:"))
b=int(input("Enter a breadth:"))
h=int(input("Enter a height:"))
s=volume(l,b,h)
print("volume of cuboid=",s)
