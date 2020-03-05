def chunk(lst1,a):
    for i in range(0,len(lst1),a):
        yield lst[i:i + a]

lst=["guru","sabarish","kumar","saravana","rakesh","anbu","balaji","captain","domain","either","further"]
n=int(input("Enter the number : "))
x=chunk(lst,n)
print(list(x))
