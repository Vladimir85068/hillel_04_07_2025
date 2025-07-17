lst = [0, 1, 0, 12, 3]

result = []
Z = 0

for z in lst:
    if z == 0:
        Z += 1
    else:
        result.append(z)

result += [0] * Z

print(result)