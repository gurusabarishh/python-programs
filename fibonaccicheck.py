num = int(input("Enter the number "))
a=0
b=1
if num==a or num==b:
    print("It's a fibonacci number")
else:
    for i in range(1,num+1):
        c=a+b
        if num==c:
            print("It's a fibonacci number")
            break
        a=b
        b=c
    else:
        print("It's not a fibonacci number")
