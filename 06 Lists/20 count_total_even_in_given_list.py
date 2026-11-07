#Write a program to count the even numbers in a list.
count_even=0
a=[12,18,38,51,27,75,91]
for x in a:
  if(x%2==0):
    count_even+=1
print("Total even number is list =",count_even)
