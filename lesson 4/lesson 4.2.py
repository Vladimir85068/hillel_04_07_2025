lst = [0, 1, 7, 2, 4, 8]

if not lst:
    result = 0
else:
    sum_even_index = 0
    for i in range(0, len(lst), 2):
        sum_even_index += lst[i]
    result = sum_even_index * lst[-1]

print(result)