a =[int(input())]
while sum(a) != 0:
    a.append(int(input()))
print(sum(i**2 for i in a))