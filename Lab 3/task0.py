spisok = [10, 120, 0, 182, -192, 4, 8, 10000, -12, 42, 45, 33, 8]
result = []
for i in range(1, len(spisok)):
    if spisok[i] > spisok[i - 1]:
        result.append(spisok[i])
print(result)