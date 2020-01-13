def large(a):
    global n
    n=len(a)
    for i in range(n-1):
        if a[i]<a[i+1]:
            continue
        a[i+1]=a[i]
    print(a[n-1])

arr=[]
n=int(input("how many numbers want to insert in array?"))
for i in range(n):
    a=int(input("Enter the number :"))
    arr.append(a)
print("largest number in array : ",end="")
large(arr)
