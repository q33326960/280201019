n = int(input("n!"))
sum,a = 1,1
for i in range(n):
    if n == 0:
        break
    sum = sum * a
    a = a + 1
zeros = 0
mod = 10
while True:
    sum % mod
    if sum % mod == 0:
        zeros = zeros + 1
        mod = mod * 10
    else:
        break
print(zeros)
