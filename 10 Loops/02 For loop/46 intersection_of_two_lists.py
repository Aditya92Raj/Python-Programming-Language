#Write a program to find the intersection of two lists.
list_01=[5,12,9,7,3,8,4]
print("list_01=",list_01,type(list_01))
list_02=[8,6,15,4,3,10,4,18]
print("list_02=",list_02,type(list_02))
intersection=[]
for x in range(len(list_01)):
    for y in range(len(list_02)):
        if list_01[x]==list_02[y] and list_01[x] not in intersection:
            intersection.append(list_01[x])
            break
print("Intersection of two list=",intersection,type(intersection))
