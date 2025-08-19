import keyword
import string

s = input().strip()

if not s:
    print(False)

elif s[0].isdigit():
    print(False)

elif any(ch.isupper() for ch in s):
    print(False)

elif any(ch not in (string.ascii_lowercase + string.digits + "_") for ch in s):
    print(False)

elif s in keyword.kwlist:
    print(False)

elif set(s) == {"_"} and len(s) > 1:
    print(False)
else:
    print(True)
