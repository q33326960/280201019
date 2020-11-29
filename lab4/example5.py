n = int(input("n "))
sum = 1
a = 1
for i in range(n):
    if n == 0:
        break
    sum = sum * a
    a = a +1
print(sum)
