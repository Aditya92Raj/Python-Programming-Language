#Write a program to count total words in a sentence.
s=0
a=input("Write a sentence:")
for x in a:
    if(x==" "):
        s+=1
print("Total words in a sentence=",s+1)
