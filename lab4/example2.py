x = int(input("Enter the year"))
if x <= 1000:
    if x % 400 == 0 and x % 4 == 0:
        print("Leap year")
elif x > 1000:
    if x % 4 ==0:
        print("Leap year")
else:
    print("Not a leap year")
