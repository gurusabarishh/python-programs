final_elements = []

Test_cases = int(input())
for i in range(Test_cases):
    lst = []
    ele_index = input().split( )
    element = input().split( )
    for j in element:
        lst.append(int(j))
    final_elements.append(lst[int(ele_index[1])])

for k in final_elements:
    print("Index element:", k)
