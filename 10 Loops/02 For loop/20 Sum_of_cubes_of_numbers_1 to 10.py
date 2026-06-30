#Write a program to find the sum of cubes of number from 1 to 10.
s=0
for x in range(1,11):
    p=x**3
    s+=p
print("Sum of cubes of numbers=",s)
