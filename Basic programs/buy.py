#function to get items
def select(ans):
    global name,quan
    lis=[]
    name = input("Enter the item :")
    quan = int(input("Enter the Quantity :"))
    lis.append([name,quan])
    return lis

#intro of items
print("Welcome to store ")
print("The items and that price is given below :")

#print the items
print("Items   -  charge per kg")
dic = {
"Rice":54,
"Pulses":171.5,
"Sugar":142,
"Millets":90.25,
"Spices":953,
"Salt":25,
"Ghee":350.75
}
for i,j in dic.items():
    print(i,j)
 
#select your items
print("\nSelect your items !!!")
a=[]
a.append(select("yes"))

#next round of selecting using function
ans="yes"
while ans=="yes":
    print("Are you want to buy another item ?(yes or no)")
    ans = input()
    if ans=="yes":
        a.append(select(ans))
print("----------------------")

#bill
print("Your Bill : ")
print("Bill No : 1 ")

print("items-quantity-rate")
total=0
for i in range(len(a)):
    print(a[i][0][0],a[i][0][1],a[i][0][1]*dic[a[i][0][0]])
    total=total+a[i][0][1]*dic[a[i][0][0]]
print("------------------------")

#total
print("total : ",total)
print("-------------------------")

#Gst
gst=total*(2/100)
print("GST (2%) :",gst)
print("-------------------------")

#total bill payable
print("Total bill payable :",total+gst)

