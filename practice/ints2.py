a,b,c = eval(input("Enter 3 numbers: "))
if a > b:
    if b > c:
        print("Spam please!")
    else:
        print("It's a late parrot!")
elif b > c:
    print ("Cheese Shop")
    if a >= c:
        print ("Cheddar")
    elif a < b:
        print ("Gouda")
    elif c == b:
        print("Swiss")
else:
    print("Trees")
    if a==b:
        print("Chestnut")
    else:
        print("larch")
print("Done")
