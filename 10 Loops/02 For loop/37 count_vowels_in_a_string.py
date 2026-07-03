#Write a program to Count vowels in a string.
count=0
string="Aditya_Raj"
for x in string:
    if x=='A' or x=='E' or x=='I' or x=='O' or x=='U' or x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
print("Total no of vowels=",count)
