n=int(input("How many elements want to insert ?"))
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
for i in range(n-1):
    if lst[i]<lst[i+1]:
        lst[i+1]=lst[i]
        a=lst[i+1]
print("Smallest number of list :",a)
