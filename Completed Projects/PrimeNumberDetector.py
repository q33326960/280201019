from colorama import Fore
def isPrime(number):
    bolen = number - 1
    if bolen <= 0:
        print("Please enter a valid integer")
        repeat()
    while bolen >= 1:
        kalan = number % bolen
        if number == 2:
            print("Duhhh don't you already know 2 is a prime number?")
            repeat()
            break
        if bolen > 1:
            if kalan == 0:
                print(Fore.RED + "It's not a prime number" + Fore.RESET)
                repeat()
                break
        if bolen == 1:
            print(Fore.GREEN +"It's a prime number!" + Fore.RESET)
            repeat()
        bolen = bolen - 1

def repeat():
    x = int(input("Enter the number to check if its prime or not "))
    isPrime(x)
repeat()
