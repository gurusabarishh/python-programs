def mean(lst, l):
    sum = 0
    for i in range(l):
        sum+=lst[i]
        print(sum//(i+1), end=" ")
    print()

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    mean(arr, n)
