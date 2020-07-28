lst=[]
n=int(input("How many numbers want to insert in list? "))
print("Enter the elements :")
for i in range(n):
    a=int(input())
    lst.append(a)
print("Positive numbers in your list :")
for j in lst:
    if (j>=0):
        print(j)
