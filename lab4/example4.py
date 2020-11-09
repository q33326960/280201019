a = int(input("a"))
b = int(input("b"))
sum =1
for i in range(b):
    sum = sum * a
    if b == 0:
        print(1)
        break
print(sum)