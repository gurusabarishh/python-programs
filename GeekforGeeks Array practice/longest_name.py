def long_name(test):
    for i in range(test):
        Lst = []
        n = int(input())
        for j in range(n):
            name = input()
            Lst.append(name)
        for k in range(n-1):
            if(len(Lst[k]) > len(Lst[k+1])):
                Lst[k], Lst[k+1] = Lst[k+1], Lst[k]
        print(Lst[n-1])
        Lst.clear()


Test_cases = int(input())
long_name(Test_cases)
