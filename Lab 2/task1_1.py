s = input() # Y4g2ke3A3BV 
r = "" # YYYYggkeeeAAABV
last = ""
for c in s:
    if c.isdigit():
        r += last * (int(c) - 1)
    else:
        r += last
        last = c
print(r)