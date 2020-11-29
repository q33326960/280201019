num1 = int(input("num1"))
num2 = int(input("num2"))
num3 = int(input("num3"))

if num1 > num2:
    if num1 > num3:
        print(num1)
elif num2 > num3:
    if num2 > num1:
        print(num2)
elif num3 > num2:
    if num3 > num1:
        print(num3)
else:
    print("Please enter diffrent numbers")