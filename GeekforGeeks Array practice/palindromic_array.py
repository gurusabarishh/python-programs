def isPalindrome(N): 
    str1 = "" + str(N) 
    for i in range(len(str1)//2): 
        if (str1[i] != str1[len(str1)- 1- i]): 
            return False
    return True

def PalinArray(arr ,n):
    for i in range(n): 
        ans = isPalindrome(arr[i]) 
        if (ans == False): 
            return False
    return True

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
