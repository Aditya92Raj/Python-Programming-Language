#Write a program to find the average of list elements.
count=0
Total=0
List=[23,45,78,96,37,69]
for x in List:
    count+=1
    Total+=x
print("Average of list element=",Total/count)
