seconds = int(input("input number seconds (0 <= n < 8640000): "))

days, remainder = divmod(seconds, 24 * 60 * 60)

hours, remainder = divmod(remainder, 60 * 60)

minutes, seconds = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "day"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    day_word = "days"
else:
    day_word = "dayss"

time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(f"{days} {day_word}, {time_str}")