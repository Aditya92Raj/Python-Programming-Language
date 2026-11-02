#Write a program to copy a list into another list.
a=[32,54,26,45,28]
print("first list =",a,type(a))
b=[]
for x in a:
  b.append(x)
print("New list =",b,type(b))
