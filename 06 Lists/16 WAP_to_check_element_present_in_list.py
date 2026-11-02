#Write a program to check whether a particular element exists in a list.
n=int(input("Enter your number:"))
a=0
List=[23,45,63,71,45,83,97]
for x in List:
  if(n==x):
    a=1
if(a==1):
  print("Your number is present in list.")
else:
  print("Your number is not present in list")
