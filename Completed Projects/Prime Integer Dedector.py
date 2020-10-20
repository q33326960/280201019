def isPrime(number):
    if number < 2:
        print("Please enter a valid integer")
        repeat()
    bolen = number - 1
    while bolen >= 1:
        kalan = number % bolen
        bolen = bolen - 1
        if bolen > 1:
            if kalan == 0:
                print("It's not a prime number")
                repeat()
                break
        if bolen == 1:
            print("It's a prime number!")
            repeat()

def repeat():
    x = int(input("Enter the number to check if its prime or not "))
    isPrime(x)
repeat()
