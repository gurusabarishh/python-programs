lst=[]
n=int(input("Enter how many elements want to insert in list :"))
for i in range(n):
    a=int(input())
    lst.append(a)
for i in range(n):
    for j in range(n):
        if lst[i]<=lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print("Asending order of the list :")
for i in lst:
    print(i)
