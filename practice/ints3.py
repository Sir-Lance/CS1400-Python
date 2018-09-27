
a,b,c = eval(input("Enter 3 numbers: "))
if a > b:
    if b > c:
        print(a)
elif b > a:
    if a > c:
        print (b)
    if c > b:
        print(c)
        #if b > a:
            #print(c)
