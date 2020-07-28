Test_cases = int(input())
Camel_case = []

for i in range(Test_cases):
    String = input()
    count = 0
    for j in String:
        if(ord(j)<=95 and ord(j)>=65):
            count = count+1
    Camel_case.append(count)
        
for k in Camel_case:
    print(k)
