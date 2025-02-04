s = input() # YYYYggkeeeAAABV
r = "" # Y4g2ke3A3BV 
last = ""
count = 0
for c in s:
    if c != last:
        if last:
            r += last
            if count > 1: r += str(count)
        count = 0
    count += 1
    last = c
r += last
if count > 1: r += str(count)
print(r)