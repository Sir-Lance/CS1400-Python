age = int(input("age: "))
cship = int(input("cship: "))

if age < 30 or cship < 9:
    print("not senator qual.")
elif age >= 30 and cship >= 9:
    print("senator qual.")
if age < 25 or cship < 7:
    print("not rep qual.")
elif age >= 25 and cship >= 7:
    print("rep qual.")
