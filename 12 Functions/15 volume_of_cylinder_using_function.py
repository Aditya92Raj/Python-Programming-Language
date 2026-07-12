#Write a function to find the volume of a cylinder.
π=22/7
def area(r,h):
    return π*r*r*h
r=int(input("Enter a radius:"))
h=int(input("Enter a height:"))
s=area(r,h)
print("volume of cylinder=",s)
