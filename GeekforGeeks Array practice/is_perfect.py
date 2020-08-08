def isperfect(lst, l):
    perfect = True
    for i in range(l//2):
        if lst[i]!=lst[-(i+1)]:
            perfect = False
            break
    if perfect == True:
        print("PERFECT")
    else:
        print("NOT PERFECT")

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    isperfect(arr, n)
