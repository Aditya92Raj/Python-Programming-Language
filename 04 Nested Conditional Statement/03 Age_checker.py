#Write a program to input age from user and check given age is miner or adult or old.
a=int(input("Enter your age:"))

if a>=18:
    if a>60:
        print("old")
    else:
        print("adult")
else:
    print("miner")
