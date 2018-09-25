def addInterest(amount, rate):
    amount *= (1 + rate)
    print("amount in addInterest" , amount)
    return amount

amount = 1000
rate = 0.05
for i in range(10):
    amount=addInterest(amount, rate)
    #print(amount)
print(amount)
