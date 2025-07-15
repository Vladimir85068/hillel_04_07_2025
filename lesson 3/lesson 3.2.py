lst =[1773, 1889, 1911, 2135]

print("Was:", lst)

if len(lst) > 1:
 last = lst.pop()
 lst.insert(0, last)

 print("Became:", lst)