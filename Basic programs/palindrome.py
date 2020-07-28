string=input()
palind=""
for i in range(len(string)-1,-1,-1):
    palind=palind+string[i]
if string==palind:
    print("This is palindrome.")
else:
    print("This not a palindrome.")
