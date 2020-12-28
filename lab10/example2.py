def heil(x):
    if x==1:
        print(1)
        return 1
    elif x % 2 == 0:
        print(int(x))
        return heil(x/2)
    else:
        print(int(x))
        return heil(3*x+1)

heil(5)