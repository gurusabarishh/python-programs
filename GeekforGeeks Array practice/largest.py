def largest(test):
    largest = []
    for i in range(test):
        size = int(input())
        elements = input().split(" ", size)
        lst = []
        for j in elements:
            lst.append(int(j))
        largest.append(max(lst))
    for i in largest:
        print(i)
        
Test_cases = int(input())
largest(Test_cases)
