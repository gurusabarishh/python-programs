lst=[1,4,3,4,5,3,7,8,3,0]
print("The list is :\n",lst)
n=int(input("Enter the any one element of this list :"))
count=0
for i in range(len(lst)):
    if n==lst[i]:
        count+=1
print("Occurence of an element :",count)
