lst = [0, 1, 7, 2, 4, 8]

result = 0
sum_even_index = 0

for i in range(0, len(lst), 2):
    sum_even_index += lst[i]
    result = sum_even_index * lst[-1]

print(result)