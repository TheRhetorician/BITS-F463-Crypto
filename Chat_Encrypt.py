import numpy as np


def SpiralOrder(A):
    mat = np.chararray((5, 5), unicode=True)
    mat[:] = 'x'
    uplimit = leflimit = 0
    lowlimit = 4
    rlimit = 4
    spiralstr = ""
    x = 0
    while x < 25:
        for i in range(rlimit, leflimit - 1, -1):
            mat[lowlimit][i] = A[x]
            spiralstr += A[x]
            x += 1
        lowlimit -= 1
        if uplimit > lowlimit:
            break
        for i in range(lowlimit, uplimit - 1, -1):
            mat[i][leflimit] = A[x]
            spiralstr += A[x]
            x += 1
        leflimit += 1
        if leflimit > rlimit:
            break
        for i in range(leflimit, rlimit + 1):
            mat[uplimit][i] = A[x]
            spiralstr += A[x]
            x += 1
        uplimit += 1
        if uplimit > lowlimit:
            break
        for i in range(uplimit, lowlimit + 1):
            mat[i][rlimit] = A[x]
            spiralstr += A[x]
            x += 1
        rlimit -= 1
        if leflimit > rlimit:
            break
    return mat, spiralstr


def RailFence(depth, str):
    rf = [['\n' for i in range(len(str))]
          for j in range(depth)]
    mode = 0
    row, col = 0, 0
    for i in range(len(str)):
        if (row == 0) or (row == depth - 1):
            mode ^= 1
        rf[row][col] = str[i]
        col += 1
        if mode == 1:
            row += 1
        else:
            row -= 1
    result = ""
    for i in range(depth):
        for j in range(len(str)):
            if rf[i][j] != '\n':
                result += rf[i][j]
    return result


t = int(input())
while t > 0:
    depth = int(input())
    PFKey = input()
    PFKey = PFKey.replace(" ", "")
    num = int(input())
    ptext = input()
    ptext = ptext.replace(" ", "")
    PFstr = ""
    for i in range(0, len(PFKey)):
        if PFstr.find(PFKey[i]) < 0:
            PFstr += PFKey[i]
    for i in range(0, 26):
        if PFstr.find("" + chr(i + ord('a'))) < 0:
            if chr(i + ord('a')) == 'i':
                if PFstr.find("j") < 0:
                    PFstr += "i"
            elif chr(i + ord('a')) == 'j':
                continue
            else:
                PFstr += ("" + chr(i + ord('a')))
    mat, spiralstr = SpiralOrder(PFstr)
    # print(mat)
    spiralstr = ""
    for row in range(0, 5):
        for col in range(0, 5):
            spiralstr += mat[row][col]
    while num > 0:
        RFstr = RailFence(depth, spiralstr)
        mat, spiralstr = SpiralOrder(RFstr)
        spiralstr = ""
        for row in range(0, 5):
            for col in range(0, 5):
                spiralstr += mat[row][col]
        num -= 1
    counter = 0
    for i in range(0, 5):
        spr = ""
        for j in range(0, 5):
            spr += (spiralstr[(i * 5) + j] + " ")
        print(spr)
    # print(PFstr)
    if PFstr.find("j") < 0:
        if ptext.find("j") >= 0:
            ptext = ptext.replace("j", "i")
    elif PFstr.find("i") < 0:
        if ptext.find("i") >= 0:
            ptext = ptext.replace("i", "j")

    plain = ""
    i = 0
    add = 0
    while i < len(ptext) - 1:
        if ptext[i] == ptext[i + 1]:
            if ptext[i] == "z":
                plain += ptext[i] + "y"
                add += 1
                i += 1
            else:
                plain += ptext[i] + "z"
                add += 1
                i += 1
        else:
            plain += ptext[i] + ptext[i + 1]
            i += 2
    if (len(ptext) + add) % 2 != 0:
        if ptext[len(ptext) - 1] == "z":
            plain += ptext[len(ptext) - 1] + "y"
        else:
            plain += ptext[len(ptext) - 1] + "z"
    # print(plain)

    cipher = ""
    for i in range(0, len(plain) - 1, 2):
        a = plain[i]
        b = plain[i + 1]
        x1 = spiralstr.find(a)
        x2 = spiralstr.find(b)
        y1 = x1 % 5
        y2 = x2 % 5
        x1 = int(x1 / 5)
        x2 = int(x2 / 5)
        if x1 == x2:
            if y1 < 4:
                cipher += spiralstr[(x1 * 5) + y1 + 1]
            else:
                cipher += spiralstr[(x1 * 5)]
            if y2 < 4:
                cipher += spiralstr[(x2 * 5) + y2 + 1]
            else:
                cipher += spiralstr[(x2 * 5)]
        elif y1 == y2:
            if x1 < 4:
                cipher += spiralstr[(x1 * 5) + y1 + 5]
            else:
                cipher += spiralstr[(y1)]
            if x2 < 4:
                cipher += spiralstr[(x2 * 5) + y2 + 5]
            else:
                cipher += spiralstr[(y2)]
        else:
            cipher += spiralstr[(x1 * 5) + y2]
            cipher += spiralstr[(x2 * 5) + y1]
    print(cipher)
    t -= 1
