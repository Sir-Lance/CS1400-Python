#p=50+5m
#if m>90
    #200+p
#total=p

m = int(input("input speed"))
p = 50 + (5 * m)
total = p

if m >= 90:
    print(p + 200)
elif m < 90:
    print(p)
