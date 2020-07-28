#find the length
strnumber = input("Enter the number : ")
order = int(len(strnumber))

#convert string into int
number = int(strnumber)

#find given number is amstrong or not amstrong
ams = 0
for i in range(order):
    ams = pow(int(strnumber[i]),order) + ams

if(ams==number):
    print("amstrong number")
else:
    print("not amstrong")
