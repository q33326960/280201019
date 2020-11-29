raweq1 = input("Enter the first equation:\n")
raweq2 = input("Enter the second equation:\n")
neweq1 = ""
neweq2 = ""
flag = False
flag2 = False
for i in raweq1:
    if i == "=":
        flag = True
    if flag == False:
        neweq1 += i
    if  flag == True:
        if i == "-":
            neweq1 += "+"
        elif i == "+":
            neweq1 += "-"
        else:
            neweq1 += i
neweq1 = neweq1.replace("=","")

for i in raweq2:
    if i == "=":
        flag2 = True
    if flag2 == False:
        neweq2 += i
    if  flag2 == True:
        if i == "-":
            neweq2 += "+"
        elif i == "+":
            neweq2 += "-"
        else:
            neweq2 += i
neweq2 = neweq2.replace("=","")

opflag = False
pos1 = ""
neg1 = ""
pos2 = ""
neg2 = ""
for i in neweq1:
    if i == "+":
        opflag = True
        if pos1 != "":
            pos1 += ","
    if i == "-":
        opflag = False
        if neg1 != "":
            neg1 += ","
    if opflag == True and i !="+":
        pos1 += i
    if opflag == False and i!= "-":
        neg1 += i

for i in neweq2:
    if i == "+":
        opflag = True
        if pos2 != "":
            pos2 += ","
    if i == "-":
        opflag = False
        if neg2 != "":
            neg2 += ","
    if opflag == True and i !="+":
        pos2 += i
    if opflag == False and i!= "-":
        neg2 += i
pos1l = pos1.split(",")
neg1l = neg1.split(",")
pos2l = pos2.split(",")
neg2l = neg2.split(",")
if "" in pos1l:
    pos1l.remove("")
if "" in pos2l:
    pos2l.remove("")
if "" in neg1l:
    neg1l.remove("")
if "" in neg2l:
    neg2l.remove("")
xk1p,yk1p,c1p,xk1n,yk1n,c1n = 0,0,0,0,0,0
xk2p,yk2p,c2p,xk2n,yk2n,c2n = 0,0,0,0,0,0
for i in pos1l:
    if "x" in i:
        xk1p += int(i.replace("x",""))
    elif "y" in i:
        yk1p += int(i.replace("y",""))
    else:
        c1p += int(i)
for i in neg1l:
    if "x" in i:
        xk1n += int(i.replace("x",""))
    elif "y" in i:
        yk1n += int(i.replace("y",""))
    else:
        c1n += int(i)
xk1 = xk1p - xk1n
yk1 = yk1p - yk1n
c1 = c1p -c1n
for i in pos2l:
    if "x" in i:
        xk2p += int(i.replace("x",""))
    elif "y" in i:
        yk2p += int(i.replace("y",""))
    else:
        c2p += int(i)
for i in neg2l:
    if "x" in i:
        xk2n += int(i.replace("x",""))
    elif "y" in i:
        yk2n += int(i.replace("y",""))
    else:
        c2n += int(i)
xk2 = xk2p - xk2n
yk2 = yk2p - yk2n
c2 = c2p -c2n
if yk1 >=0:
    yk1 = "+" + str(yk1)
if yk2 >=0:
    yk2 = "+" + str(yk2)
print("Equations in the simplified form:")
print(f"{xk1}x{yk1}y={-c1}")
print(f"{xk2}x{yk2}y={-c2}")
yk2 = int(yk2)
yk1 = int(yk1)
sx,sy = 0,0
if yk1 != 0:
    coef = yk2/yk1
    sx = ((-coef*-c1)+ -c2) / ((xk1*-coef) + xk2)
    sy = (-c1 -(xk1*sx)) / yk1
else:
    sx = -c1 / xk1
    sy = (-c2 - (xk2*sx)) / yk2

sx=int(sx)
sy=int(sy)
print("Solution:")
print(f"x={sx}")
print(f"y={sy}")