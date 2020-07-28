num1 = int(input("Enter the starting number :"))
num2 = int(input("Enter the end number :"))
for i in range(num1,num2+1):
    if i%2 == 0:
        print (i,"is even number")
    else:
        print (i,"is odd number")
