x = input("num1: ")
y = input("num2: ")
common = list()
for i in x:
    for _ in y:
        if i in y:
            if int(i) not in common:
                common.append(int(i))
print(common)
            