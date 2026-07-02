#Write a program to print tables from 1 to 5.
for x in range(1,6):
    print(f"Table of {x}")
    for y in range(1,11):
        print(f"{x}*{y}=",x*y)
        if y==10:
            print("\n")
