x = input("num1: ")
y = input("num2: ")
common = list()
for i in x:
    for _ in y:
        if i in y:
            if i not in common:
                common.append(i)
print(common)
            