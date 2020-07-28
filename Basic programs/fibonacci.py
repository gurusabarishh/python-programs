num=int(input("Enter the ending number :"))
a=0
b=1
if num==1:
    print(a)
else:
    if num==2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(1,num-1):
            c=a+b
            print(c)
            a=b
            b=c
