spisok = eval(input()) # ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
d = {}
for x in spisok:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(" ".join(list(map(str, d.values()))))