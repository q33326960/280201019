def selectionSort(list):
    minx = None
    count = 0
    for x in range(len(list)):
        for i in list[count:]:
            if  minx == None or i < minx:
                minx = i
        print(minx)
        cindex = list.index(minx)
        temp = list[count]
        list[count] = minx
        list[cindex] = temp
        count += 1
sa = [19,-3,4,24,12,7,9,69,0,16,35,42,63]
selectionSort(sa)
print(sa)


