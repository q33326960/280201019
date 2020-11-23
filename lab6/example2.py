s = int(input("student quantity: "))
ml = list()
for i in range(s):
    m1 = int(input("midterm1"))
    m2 = int(input("midterm2"))
    f = int(input("final"))
    ml.append([m1,m2,f])
a = int(input("AVG of std x"))
for i in ml[a -1]:
    count = 0
    sum = 0
    if count == 0:
        sum += i *3/10
    elif count == 1:
        sum += i *3/10
    elif count == 2:
        sum += i *4/10
    count += 1
print(sum)