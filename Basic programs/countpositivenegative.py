n=int(input("How many numbers want to insert in list? "))
lst=[]
negative=positive=0
print("Enter the elements ")
for i in range(n):
    a=int(input())
    lst.append(a)
for i in lst:
    if i<0:
        negative+=1
    else:
        positive+=1
print("Count of negative numbers in list :",negative)
print("Count of positive numbers in list :",positive)
