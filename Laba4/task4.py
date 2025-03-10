s = input()
d = {int(x): s.count(x) for x in "0123456789"}
print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]))