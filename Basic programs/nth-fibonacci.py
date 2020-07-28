num = int(input("Enter the number :"))
a=0
b=1
print("n'th fibonacci number =",end="")
if num==1:
    print(a)
elif num==2:
    print(b)
else:
    for i in range(1,num-1):
        c=a+b
        a=b
        b=c
print(c)
