def rotation(a):
    global n
    m=int(input("How many times want to rotate :"))
    for i in range(m):
        print(i+1,"time rotation :")
        b=a[0]
        for j in range(n-1):
            a[j]=a[j+1]
        a[n-1]=b
        print(a)

arr=[]
n=int(input("how many numbers want to insert in array?"))
for i in range(n):
    a=int(input("enter the number :"))
    arr.append(a)
rotation(arr)
