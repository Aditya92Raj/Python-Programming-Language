#Write a program to input the time (24-hour format) and it is morning, Afternoon, Evening or Night.
t=int(input("Enter your time:"))
if t>=0 and t<=23:
    if t<6:
        print("Night")
    elif t<12:
        print("Morning")
    elif t<16:
        print("Afternoon")
    elif t<20:
        print("Evening")
    else:
        print("Night")
else:
    print("Invalid Time")
