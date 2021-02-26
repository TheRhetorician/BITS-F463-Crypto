import numpy as np


def conv(c):
    x = ord(c)
    if x >= 97 and x <= 122:
        return x - 87
    elif x >= 48 and x <= 57:
        return x - 48


ctext = input()
l = len(ctext)
if l % 2 == 0:
    n = int((l) / 2)
else:
    n = int((l + 1) / 2)

answer = "" + ctext[0]
for i in range(1, n):
    answer += hex(conv(ctext[i]) ^ conv(ctext[i - 1]))[2:]
print(answer)
