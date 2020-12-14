import random
def randlist(x,y,z):
    rndlist= list()
    for i in range(x):
        rndlist.append(random.randint(y,z))
    return rndlist
def inter(x,y):
    inter = list()
    for i in x:
        if i in y:
            inter.append(i)
    return inter
def main(x,y,z):
    l1 =randlist(x,y,z)
    l2 =randlist(x,y,z)
    print(inter(l1,l2))
main(8,1,10)