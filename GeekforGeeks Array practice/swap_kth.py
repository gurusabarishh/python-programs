def swap(lst, l):
    lst[l[-1]-1], lst[-l[-1]] = lst[-l[-1]], lst[l[-1]-1]
    for i in range(l[0]):
        print(lst[i], end=" ")
    print()

T = int(input())
for i in range(T):
    n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    swap(arr, n)
