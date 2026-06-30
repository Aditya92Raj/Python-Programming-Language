#Write a program to find the sum of multiples of 5 from 1 to 100.
s=0
for x in range(5,101,5):
    s+=x
print("Sum of multiples of 5=",s)
