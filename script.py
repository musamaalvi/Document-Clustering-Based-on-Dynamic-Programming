
DS1 = ["love","play"]
DS2 = ["love", "play", "cricket", "hate", "hockey"]
DS3 = ["Pakistan1", "boy1", "love1", "cricket1", "hockey1"]
DS4 = ["love", "play", "cricket", "hate", "hockey"]
DS5 = ["Pakistan1", "boy1", "love1", "cricket1", "hockey1"]
DS6 = ["love", "play", "cricket", "hate", "hockey"]
DS7 = ["Pakistan1", "boy1", "love1", "cricket1", "hockey1"]


k = 3
c = []
c.append(DS1)
c.append(DS2)
c.append(DS3)
c.append(DS4)
c.append(DS5)
c.append(DS6)
c.append(DS7)


#####
cc=[]

def CTAS(w1, x, y, CTPF):
    x = x + 1
    y = y + 1
    if len(CTPF) == 0:
        tup = (w1, x, "DS1", y, "DS2")
        CTPF.append(tup)
        return 1 / ((x) * (y))
    tup = (w1, x, "DS1", y, "DS2")
    CTPF.append(tup)
    return 1 / ((CTPF[-1][1] - CTPF[-2][1]) * (CTPF[-1][3] - CTPF[-2][3]))


def SSM(DS1, DS2):
    CTPF = []
    m = len(DS1)
    n = len(DS2)
    processed = []
    sum = 0;
    SCS = 0
    for curX in range(0, m):
        for curY in range(0, n):
            if (DS2[curY] not in processed and DS2[curY] == DS1[curX]):
                temp = CTAS(DS1[curX], curX, curY, CTPF)
                SCS = SCS + temp
                # print (temp)
                processed.append(DS2[curY])
                sum = sum + 1
    if (SCS == 0):
        return 0
    else:
        return SCS / sum




def callFormulaForSingle(c1, c2):
    sum = 0
    sum = sum + SSM(c1, c2)

    valueWithPlus = 0;

    if sum != 0:
        valueWithPlus = valueWithPlus + (sum / 2)
    return (valueWithPlus)


def callFormulaForMoreThanSingle(c1, c2):
    finalvalue = 0;
    #if len(c1) != 1 or len(c1[0]) != 0:
    sum = 0
    for i in range(0, len(c1)):
        for j in range(i + 1, len(c1)):
            sum = sum + SSM(c1[i], c1[j])
            print(finalvalue)
    if sum != 0:
        finalvalue = finalvalue + (sum / len(c1))
    #if len(c2[0]) != 1 or len(c2[0]) != 0:
    sum = 0
    for i in range(0, len(c2)):
        for j in range(i + 1, len(c2)):
            sum = sum + SSM(c2[i], c2[j])
            print(finalvalue)
    if sum != 0:
        finalvalue = finalvalue + (sum / len(c2))
    tc = c1 + c2
    valueWithPlus = 0;
    if tc != 0 or tc != 1:
        sum = 0
        for i in range(0, len(tc)):
            for j in range(i + 1, len(tc)):
                sum = sum + SSM(tc[i], tc[j])
                print(valueWithPlus)
        if sum != 0:
            valueWithPlus = valueWithPlus + (sum / len(tc))
    return ((finalvalue * (-1)) + valueWithPlus)


def callFormulaForOneSingle(c1, c2):
    finalvalue = 0;

    if len(c2[0]) != 1 or len(c2[0]) != 0:
        sum = 0
        for i in range(0, len(c2)):
            for j in range(i + 1, len(c2)):
                sum = sum + SSM(c2[i], c2[j])
                print(finalvalue)
        if sum != 0:
            finalvalue = finalvalue + (sum / len(c2))
    tc = [c1] + c2
    valueWithPlus = 0;
    if tc != 0 or tc != 1:
        sum = 0
        for i in range(0, len(tc)):
            for j in range(i + 1, len(tc)):
                sum = sum + SSM(tc[i], tc[j])
                print(valueWithPlus)
        if sum != 0:
            valueWithPlus = valueWithPlus + (sum / len(tc))
    return ((finalvalue * (-1)) + valueWithPlus)



totalClusters = len(c);

cf = 0.0
while totalClusters > k:
    m = 1
    n = 1

    max=-999999999
    for i in range(0, len(c)):
        for j in range(i + 1, len(c)):
            if type(c[i][0]) == str and type(c[j][0]) == str:
                temp = callFormulaForSingle(c[i], c[j])
                if (temp  > max):
                    max = temp
                    m = i
                    n = j
                # if (cff > cf):
                #     m = i
                #     n = j
                #     cf = cff
            elif type(c[i][0]) == list and type(c[j][0]) == list:
                # cff = cf + callFormulaForMoreThanSingle(c[i], c[j])
                temp = callFormulaForMoreThanSingle(c[i], c[j])
                if (temp > max):
                    max = temp
                    m = i
                    n = j

            elif type(c[i][0]) == str and type(c[j][0]) == list:
                # cff = cf + callFormulaForOneSingle(c[i], c[j])
                temp = callFormulaForOneSingle(c[i], c[j])
                if (temp > max):
                    max = temp
                    m = i
                    n = j

            else:
                # cff = cf + callFormulaForOneSingle(c[j], c[i])
                temp = callFormulaForOneSingle(c[i], c[j])
                if (temp > max):
                    max = temp
                    m = i
                    n = j
    cff = cf + max


    if type(c[m][0]) == str and type(c[n][0]) == str:
        lst1 = c.pop(m)
        lst2 = c.pop(n - 1)
        lst = []
        lst.append(lst1)
        lst.append(lst2)
        c.append(lst)
    elif type(c[m][0]) == list and type(c[n][0]) == list:
        lst1 = c[m]
        lst2 = c[n]
        del c[m]
        del c[n - 1]
        c.append(lst1+lst2)
    elif type(c[m][0]) == str and type(c[n][0]) == list:
        lst1 = c.pop(m)
        lst2 = c[n - 1]
        del c[n - 1]
        lst2.append(lst1)
        c.append(lst2)
    else:
        lst1 = c.pop(n)
        lst2 = c[m]
        del c[m]
        lst2.append(lst1)
        c.append(lst2)
    totalClusters = len(c)

for i in range(0, len(c)):
    print(str(c[i]))


