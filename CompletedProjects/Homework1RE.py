raweq1 = "+5x+5y=+18-3x"
raweq2 = "+4y+5x=+3y-18"
def getCoefList(equation):
    pos =""
    neg = ""
    opeq= ""
    flag = False  
    for i in equation:              
        if i == "=":
            flag = True
        if flag == True:
            if i == "+":
                opeq += "-"
            elif i == "-":
                opeq += "+"
            else:
                opeq += i
        else:
            opeq += i
    opeq = opeq.replace("=","")
    flag = False
    print(opeq)
    for i in opeq:
        if i == "+":
            flag = True
            if pos != "": pos += ","
            continue
        elif i == "-":
            flag = False
            if neg != "": neg += ","
            continue
        if flag == True:
            pos += i
        if flag == False:
            neg += i
    posl = pos.split(",")
    negl = neg.split(",")
    return posl, negl

def GetCoef(posl,negl):
    xkp,ykp,cp,xkn,ykn,cn = 0,0,0,0,0,0
    for i in posl:
        if "x" in i:xkp += int(i.replace("x",""))        
        elif "y" in i:ykp += int(i.replace("y",""))        
        else:cp += int(i)
    for i in neg1l:
        if "x" in i:xkn += int(i.replace("x",""))        
        elif "y" in i:ykn += int(i.replace("y",""))        
        else:cn += int(i)
    xk = xkp - xkn
    yk = ykp - ykn
    c = cp -cn
    return xk,yk,c
posl1,neg1l = getCoefList(raweq1)
pos2l,neg2l = getCoefList(raweq2)
a,b,c=GetCoef(posl1,neg1l)
d,e,f=GetCoef(pos2l,neg2l)
