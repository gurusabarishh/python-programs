def check(lst, l, sm):
    count = 0
    for i in range(l):
        if(lst[i]<=sm):
            count+=1
    print(count)


T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ele = int(input())
    check(arr, n, ele)
