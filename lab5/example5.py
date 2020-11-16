x = int(input("Enter the desired amount of number so show in fibonacci sequence: "))
a = 0
b = 1
for i in range(x-2):
    if i ==0:
        print(0)
    if i ==1:
        print(1)
    c =  a + b
    print(c)
    a = b
    b = c
