#Write a function to find the volume of a cube.
def volume(a):
    return a*a*a
a=int(input("Enter a side:"))
s=volume(a)
print("volume of cube=",s)
