x = int(input("Enter the year"))
if x % 100 == 0:
    if x % 400 == 0 and x % 4 == 0:
        print("Leap year")
    else:
        print("not")
elif x % 100 != 0 :
    if x % 4 ==0:
        print("Leap year")
    else:
        print("not")
