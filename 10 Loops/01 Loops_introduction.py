#Loops in python:-
#Loop is used repeat a block of code multiple times.
#There are two types of loop:-
#(i)for loop
#(ii)while loop
a=[4,6,3,5,7]
print("List=",a)
print(type(a))
for i in a:
  print(i)
b=1
n=int(input("Enter a number for table:"))
while b<=10:
    print(n*b)
    b+=1
