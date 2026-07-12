#Write a function to find the area of a circle.
π=22/7
def area(r):
    return π*r*r
r=int(input("Enter a radius:"))
s=area(r)
print("area of circle=",s)
