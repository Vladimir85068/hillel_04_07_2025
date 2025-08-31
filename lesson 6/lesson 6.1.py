s = input("Input letters: ")
start, end = s.split("-")

result = ""
for code in range(ord(start), ord(end) + 1):
    result += chr(code)

print(result)