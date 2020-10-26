gpa = float(input("gpa"))
lec = int(input("lec"))

if gpa >= 2.0 :
    if lec >= 47:
        print("congrats")
else:
    print("not enough lectures")

if gpa < 2:
    if lec >= 47:
        print("not enogh gpa")
else:
    print("not enough gpa or lectures")


