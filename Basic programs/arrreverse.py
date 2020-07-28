def reverse(a):
    global n
    for i in range(n-1,-1,-1):
        print(a[i])

arr=[]
n=int(input("how many numbers want to insert in array ?"))
for i in range(n):
    a=int(input("Enter the number :"))
    arr.append(a)
reverse(arr)
