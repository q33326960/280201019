def ex1():
    cover = eval(input("Cover price: "))
    price = cover * 6 / 10
    desiredAmount = int(input("Desired amount of books: "))
    sumPrice = (price * desiredAmount) + (desiredAmount - 1) * 0.75 + 3
    print(sumPrice)


