def check(lst, l):
    for i in range(l):
        if lst[0]<=lst[i]:
            sort = 1
        else:
            sort = 0
            break
    print(sort)

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    check(arr, n)
