def listswap(lis,first,second):
    lis[first],lis[second]=lis[second],lis[first]
    print(lis)

lis=[]
n=int(input("how many elements want to insert in list? "))
for i in range(n):
    a=input("Enter the element :")
    lis.append(a)

print("What elements want to swap? \nEnter element's place :")
b=int(input())
c=int(input())
print("The swapped form of list :")

listswap(lis,b-1,c-1)
