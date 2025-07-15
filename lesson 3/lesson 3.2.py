lst =[1773, 1889, 1911, 2135]

print("Was:", lst)

if len(lst) > 1:
 lst.insert(0, lst[-1])
 lst.pop(4)

 print("Became:", lst)