#Write a program to print all elements of list in reverse order.
List=[23,45,54,75,89,91,67]
print("Given List=",List)
print("List in reverse order is below:-")
for x in range(len(List)-1,-1,-1):
    print(List[x])
