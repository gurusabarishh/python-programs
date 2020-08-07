def check(lst, n):
    small, large = 0, 0
    for i in range(n[0]):
        if n[-1]>lst[i]:
            small+=1
        elif n[-1]<lst[i]:
            large+=1
        else:
            small+=1
            large+=1
    print(small, large)

T = int(input())
for i in range(T):
    nums = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    check(arr, nums)
