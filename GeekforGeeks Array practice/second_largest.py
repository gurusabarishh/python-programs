def secondlarge(test):
    largest = []
    for i in range(test):
        lst = []
        index = []
        size = int(input())
        elements = input().split(" ", size)
        for j in elements:
            try:
                lst.append(int(j))
            except:
                pass
        mx = max(lst)
        for k in range(len(lst)):
            if(lst[k]==mx):
                index.append(k)
        for l in index:
            lst.pop(l)
        largest.append(max(lst))
    for i in largest:
        print(i)

Test_cases = int(input())
secondlarge(Test_cases)
