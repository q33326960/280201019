def greet(dil):
    if dil == "tr":
        print("Selam")
    elif dil == "en":
        print("Hi")
    elif dil == "ch":
        print("Welcome to the Rice Fields motherfucker")
    elif dil == "jp":
        print("Yamete onii-chan itaiiii")
    else:
        print("I don't know what garbage language you are talking")

greet("ch")
greet("tr")
greet("jp")
greet("es")

def greet2(dil):
    if dil == "tr":
       return "SEA"
print(greet2("tr"))

def hipotenus(a,b):
    c = (a**2 + b**2)**0.5
    return c
print(hipotenus(3,4))
