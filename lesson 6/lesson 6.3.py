n = int(input("Put number: "))

while n > 9:
    product = 1
    for digit in str(n):
        product *= int(digit)
    n = product

print(n)