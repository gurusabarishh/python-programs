string=input().split()
for i in range(len(string)-1,-1,-1):
    for j in string[i]:
        print(j,end="")
    print(" ",end="")
