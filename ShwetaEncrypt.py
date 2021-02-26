import numpy as np

ct = input()
th, he = input().split()

Cmat = np.array([[ord(th[0]) - ord('A'), ord(th[1]) - ord('A')],
                 [ord(he[0]) - ord('A'), ord(he[1]) - ord('A')]])
# print(Cmat)
ConjPmat = np.array([[ord('E') - ord('A'), (-1) * (ord('H') - ord('A'))],
                     [(-1) * (ord('H') - ord('A')), ord('T') - ord('A')]])
# print(ConjPmat)

for row in range(0, 2):
    for col in range(0, 2):
        if ConjPmat[row][col] < 0:
            ConjPmat[row][col] += 26
# print(ConjPmat)

det = (ord('T') - ord('A')) * (ord('E') - ord('A')) - \
    (ord('H') - ord('A')) * (ord('H') - ord('A'))
# print(det)
i = 1
while 1 > 0:
    if (i * det) % 26 == 1:
        break
    else:
        i += 1
invdet = i
# print(invdet)

ConjPmat = invdet * ConjPmat
# print(ConjPmat)
for row in range(0, 2):
    for col in range(0, 2):
        if ConjPmat[row][col] >= 26:
            ConjPmat[row][col] %= 26
# print(ConjPmat)

Key = np.dot(ConjPmat, Cmat)
for row in range(0, 2):
    for col in range(0, 2):
        if Key[row][col] >= 26:
            Key[row][col] %= 26
# print(Key)

detKey = Key[0][0] * Key[1][1] - Key[0][1] * Key[1][0]
# print(detKey)

if detKey < 0:
    detKey = detKey % 26

i = 1
while 1 > 0:
    if (i * detKey) % 26 == 1:
        break
    else:
        i += 1
invdetKey = i
# print(invdetKey)
temp = Key[0][0]
Key[0][0] = Key[1][1]
Key[0][1] *= (-1)
Key[1][0] *= (-1)
Key[1][1] = temp

for row in range(0, 2):
    for col in range(0, 2):
        if Key[row][col] < 0:
            Key[row][col] += 26

Key = invdetKey * Key
# print(Key)
for row in range(0, 2):
    for col in range(0, 2):
        if Key[row][col] >= 26:
            Key[row][col] %= 26
# print(Key)
ctlen = len(ct)
if ctlen % 2 != 0:
    ctlen += 1
    ct += 'Z'
# print(ct)
answer = ""
for i in range(0, ctlen - 1, 2):
    Cstar = np.array([[ord(ct[i]) - ord('A')],
                      [ord(ct[i + 1]) - ord('A')]])
    #Pstar = Key * Cstar
    # print(Cstar)
    Pstar = np.array([[Cstar[0][0] * Key[0][0] + Cstar[1][0] * Key[1][0]],
                      [Cstar[0][0] * Key[0][1] + Cstar[1][0] * Key[1][1]]])
    for row in range(0, 2):
        for col in range(0, 1):
            if Pstar[row][col] >= 26:
                Pstar[row][col] %= 26
            answer += (chr(Pstar[row][col] + ord('A')))
print(answer)
