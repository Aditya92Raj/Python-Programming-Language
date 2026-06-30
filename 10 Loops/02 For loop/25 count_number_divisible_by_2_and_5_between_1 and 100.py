#Write a program to count numbers divisible by both 2 and 5.
s=0
for x in range(5,101,5):
    if x%2==0:
        s+=1
print("Total no of divisible by 2 and 5 =",s)
