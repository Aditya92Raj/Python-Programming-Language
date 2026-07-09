#Write a program to find the union of two lists.
list_01=[5,12,9,7,3,8,4]
print("list_01=",list_01,type(list_01))
list_02=[8,6,15,4,3,10,4,18]
print("list_02=",list_02,type(list_02))
union=[]
for x in range(len(list_01)):
    if list_01[x] not in union:
        union.append(list_01[x])
for x in range(len(list_02)):
    if list_02[x] not in union:
        union.append(list_02[x])
print("union of two list=",union,type(union))
