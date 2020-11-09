x = int(input("Enter the integer: "))
if x < 10 :
    print(x)
else:
    a = x % 10
    b = (x % 100 - a) // 10
    y = a +b
    print(a)
    print(b)
    print(y)
