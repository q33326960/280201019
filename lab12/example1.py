def selectionSort(list):
    count = 0
    for _ in range(len(list)):
        minx = None
        for i in list[count:]:
            if  minx == None or i < minx:
                minx = i
        cindex = list.index(minx)
        temp = list[count]
        list[count] = minx
        list[cindex] = temp
        count += 1
sa = [19,-3,4,24,12,7,9,69,0,16,35,42,63]
selectionSort(sa)
print(sa)
my_list = [22, 8, 12, -4, 27, 30, 36, 50, 7, 68, 91, 56, 2, 85, 42, 98, 25]
selectionSort(my_list)
print(my_list)

