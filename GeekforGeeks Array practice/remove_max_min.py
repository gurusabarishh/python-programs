def remove(lst, l):
    for i in range(l-1):
        if(i%2==0):
            lst.remove(max(lst))
        else:
            lst.remove(min(lst))
    print(lst[0])

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    remove(arr, n)
