lst=[]
repeat=[]
n=int(input("How many want to insert in list? "))
for i in range(n):
    a=int(input())
    lst.append(a)
for j in range(n):
    for k in range(j+1,n):
        if lst[j]==lst[k] and lst[j] not in repeat:
            repeat.append(lst[j])
print("repeated numbers :",repeat)
