def bs(list,item):
    if len(list) == 0:
        return "not found"
    else:
        midpoint = len(list)//2
        if list[midpoint] == item:
            return sa.index(item)
        elif item < list[midpoint]:
            return bs(list[:midpoint],item)
        else:
            return bs(list[midpoint+1:],item)
sa = [19,-3,4,24,12,7,9,69,0,16,35,42,63]
sa = sorted(sa)
print(sa)
print(bs(sa,63))