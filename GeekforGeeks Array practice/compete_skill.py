def score(lst, lst1):
    a_score = 0
    b_score = 0
    for i in range(len(lst)):
        if lst[i]>lst1[i]:
            a_score+=1
        elif lst[i]==lst1[i]:
            pass
        else:
            b_score+=1
    print(a_score, b_score)

T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    score(arr, arr1)
