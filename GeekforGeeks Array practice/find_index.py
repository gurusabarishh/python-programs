def index(lst, l, ele):
    index = []
    for i in range(l):
        if lst[i]==ele:
            index.append(i)
    if len(index)==0:
        print(-1)
    else:
        print(index[0], index[-1])

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    num = int(input())
    index(arr, n, num)
