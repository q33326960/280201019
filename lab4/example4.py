a = int(input("a"))
b = int(input("b"))
sum =1
for i in range(b):
    sum = sum * a
    if b == 0:
        sum = 1
        break
print(sum)