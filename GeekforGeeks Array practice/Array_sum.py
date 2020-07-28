Test_cases = int(input())
Array_Sum = []

for i in range(Test_cases):
    Lst = []
    size = int(input())
    elements = input().split(" ", size)
    for j in elements:
        Lst.append(int(j))
    Array_Sum.append(sum(Lst))

for k in Array_Sum:
    print(k)
