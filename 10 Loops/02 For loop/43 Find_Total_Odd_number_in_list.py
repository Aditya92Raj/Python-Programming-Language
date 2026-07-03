#Write a program to print all Odd number elements of a list.
count=0
List=[23,45,78,96,37,69]
for x in List:
    if x%2==0:
        continue
    else:
        count+=1
print("Total Odd element in list=",count)
