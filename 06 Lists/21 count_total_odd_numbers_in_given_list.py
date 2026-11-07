#Write a program to count the odd numbers in a list.
count_odd=0
a=[12,18,38,51,27,75,91]
for x in a:
  if(x%2!=0):
    count_odd+=1
print("Total odd numbers in list =",count_odd)
