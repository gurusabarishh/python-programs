def array(lst, l):
    for i in range(l-1,-1,-1):
        print(lst[i],end=" ")
    print()

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    array(arr, n)
