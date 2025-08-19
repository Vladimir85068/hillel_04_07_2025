import string

strg = input("Input a string: ")

if not strg.strip():
    exit()

for zx in string.punctuation:
    strg = strg.replace(zx, "")

hashtag = '#'
for xz in strg.split():
    if xz:
        hashtag += xz[0].upper() + xz[1:]

print(hashtag[:140])