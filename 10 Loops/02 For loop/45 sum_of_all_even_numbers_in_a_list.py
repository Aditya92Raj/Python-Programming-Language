#Write a program to print all sum of all even number elements of a list.
s=0
List=[23,45,78,96,37,69]
for x in List:
    if x%2==0:
        s+=x
print("Sum of even number=",s)
