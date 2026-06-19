#Conditional Statement in python(if,elif and else)
marks=int(input("enter your marks:"))
if marks>=80 and marks<=100:
    print("First")
elif marks<80 and marks>=50:
    print("Second")
elif marks<50 and marks>=30:
    print("Third")
elif marks<30 and marks>0:
    print("Fail")
else:
    print("error...")
