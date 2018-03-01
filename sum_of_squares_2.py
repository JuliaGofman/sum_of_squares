a = int(input())
s, sq = a, a ** 2
while s != 0:
    a = int(input())
    sq += a ** 2
    s += a
print(sq)