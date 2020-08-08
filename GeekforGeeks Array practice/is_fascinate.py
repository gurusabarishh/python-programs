def isfascinate(num):
    if len(str(num))==3:
        fasci_num = str(num) + str(num*2) + str(num*3)
        fasci_lst = []
        digits = [1,2,3,4,5,6,7,8,9]
        for i in range(len(fasci_num)):
            fasci_lst.append(int(fasci_num[i]))
        for j in digits:
            if j in fasci_lst:
                fasci = "Fascinating"
            else:
                fasci = "Not Fascinating"
                break
        print(fasci)
    else:
        print("Number should be atleast three digits")

T = int(input())
for i in range(T):
    n=int(input())
    isfascinate(n)
