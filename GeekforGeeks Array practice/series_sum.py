def sumseries(num):
    sum = 0
    for i in range(1,num+1,1):
        sum += i
    print(sum)
    

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        sumseries(n)
