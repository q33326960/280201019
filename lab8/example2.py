def isPrime(x):
    flag = True
    for i in range(2,x):
        if x % i ==0:
            flag = False
    return flag

def print_between(x,y):
    for i in range(x,y+1):
        if isPrime(i):
            print(i)
print_between(5,27)
