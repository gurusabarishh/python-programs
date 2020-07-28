def add(a):
    sum=0
    for i in a:
        sum = i+sum
    print(sum)
arr=[]
n=int(input("how many numbers want to input?"))
for i in range(n):
    a=int(input("Enter the number :"))
    arr.append(a)
print("Sum of array :",end="")
add(arr)
