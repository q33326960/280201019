list = [1,2,3,4]
def rev(list):
    if len(list) ==0:
        return []
    else:
        return [list.pop()] + rev(list)
print(rev(list))