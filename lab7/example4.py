emp_dict = dict()
for i in range(5):
    proleter = input("Proleter: ")
    maas = int(input("Maas:"))
    emp_dict[proleter] = maas
sortedl=sorted(emp_dict.items(), key=lambda x:x[1], reverse=True)
for i in range(3):
    print(sortedl[i])