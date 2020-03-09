test_str = "GeeksForGeeks"
print (test_str)  
new_str ="" 
n=int(input())
for i in range(len(test_str)): 
	if i != n-1: 
		new_str = new_str + test_str[i] 
print (new_str) 
