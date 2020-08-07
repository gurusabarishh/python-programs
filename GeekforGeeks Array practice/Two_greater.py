def sort(lst, l):
    for i in range(l):
        for j in range(l-1-i):
            if(lst[j]>lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    lst.pop(-1)
    lst.pop(-1)
    for i in lst:
        print(i,end=" ")
    print()


T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    sort(arr, n)
