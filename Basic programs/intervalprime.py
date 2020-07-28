def prime(num1,num2):
    if num1<0 or num2<0:
        print("you entered the negative number")
    else:
        print("Prime numbers :")
        for i in range(num1,num2+1):
            if i==2:
                print(i)
            elif i==1 or i==0:
                continue
            else:
                for j in range(2,i):
                    if (i%j==0):
                        break
                else:
                    print(i)

a = int(input("Enter the starting number :"))
b = int(input("Enter the ending number :"))
prime(a,b)
