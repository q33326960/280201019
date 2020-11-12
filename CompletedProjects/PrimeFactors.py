def isPrime(list):
    primeFactors = []
    for i in list:
        bolen = i -1
        while bolen >= 1:
            kalan = i % bolen
            if bolen > 1:
                if kalan ==0:
                    break
            if bolen == 1:
                primeFactors.append(i)
            bolen = bolen -1
    print(primeFactors)

def PrimeFactors(number):
    factors = []
    for i in range(number):
        if number % (i+1) == 0:
            factors.append(i+1)
    return factors

def loop():
    x = int(input("Enter the number:"))
    isPrime(PrimeFactors(x))
    loop()
loop()