list=[1,2,3,4,5,6,8]
def even(list):
    if len(list) == 0:
        return 0
    else:
        if list[0] % 2 ==0:
            return 1 + even(list[1::])
        else:
            return even(list[1::])
print(even(list))