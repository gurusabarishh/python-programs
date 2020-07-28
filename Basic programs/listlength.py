lst = ["A","guru","sabarish","kumar"]
last=lst[-1]

length=0
for i in lst:
    length=length+1
    if i == last:
        break
print("The length of list :",length)

