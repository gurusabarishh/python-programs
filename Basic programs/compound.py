principle = float(input("principle :"))
time = float(input("time : "))
rate = float(input("rate : "))
a= (1+(rate/100))**time
a= pow(1+(rate/100),time)
compound = principle*a
print("compound intrest = ",compound)
