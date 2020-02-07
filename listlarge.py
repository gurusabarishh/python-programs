n=int(input("How many numbers wabt to insert in list :"))
lst=[]
print("Emter the elements :")
for i in range(n):
    a=int(input())
    lst.append(a)
for i in range(n-1):
    if lst[i]>lst[i+1]:
        lst[i+1]=lst[i]
    large=lst[i+1]
print("largest number in list :",large)
