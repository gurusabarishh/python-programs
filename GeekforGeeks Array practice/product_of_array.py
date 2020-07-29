def product(test):
    products = []
    for i in range(test):
        lst = []
        size = int(input())
        elements = input().split(" ", size)  #get the elements
        # find the product
        multi = 1
        for j in elements:
            try:
                multi = multi*int(float(j))
            except:
                pass
        products.append(multi)
        elements.clear()
        lst.clear()
    #print the product    
    for i in products:
        print(i)

Test_cases = int(input())
product(Test_cases)
