lst=[]
n=int(input("How many numbers want to insert in the list :"))
for i in range(n):
    a=int(input())
    lst.append(a)
multi=1
for i in lst:
    multi=multi*i
print("Multiplication of the elements in list =",multi)
