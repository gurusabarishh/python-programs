lst=[]
n=int(input("How many numbers want to insert in list :"))
for i in range(n):
    a=int(input())
    lst.append(a)
sum=0
for i in lst:
    sum=sum+i
print("Sum of the list elements =",sum)
