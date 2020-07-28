lst=[1,2,3,4,5,6,7,8,9,0]
exist=int(input("Enter your element :"))
for i in lst:
    if exist==i:
        print("Your input element is exist in the list")
        break
else:
    print("Your input element is not exist in the list")
