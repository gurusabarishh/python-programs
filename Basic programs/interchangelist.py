lis = []
n=int(input("How many nnumbers want to insert in a list? "))
        
for i in range(n):
    b=input("Enter the element :")
    lis.append(b)
lis[0],lis[(len(lis)-1)]=lis[(len(lis)-1)],lis[0]
print(lis)
