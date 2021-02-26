import numpy as np

keystr = input()
ptext = input()

Key = np.arange(9)
Key = Key.reshape(3, 3)

i = 0
for j in range(0, 3):
    for k in range(0, 3):
        Key[j][k] = ord(keystr[i]) - ord('a')
        i += 1
# print(Key)
Pmat = np.arange(3)
Pmat = Pmat.reshape(3, 1)

i = 0
for j in range(0, 3):
    Pmat[j][0] = ord(ptext[i]) - ord('a')
    i += 1
# print(Pmat)
Cmat = np.dot(Key, Pmat)
# print(Cmat)
answer = ""
for j in range(0, 3):
    if Cmat[j][0] >= 26:
        Cmat[j][0] %= 26
        answer += (chr(Cmat[j][0] + ord('a')))
print(answer)
