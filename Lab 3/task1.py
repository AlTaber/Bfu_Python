spisok = [10, 120, 0, 182, -192, 4, 8, 10000, -12, 42, 45, 33, 8]
index_max = spisok.index(max(spisok))
index_min = spisok.index(min(spisok))
spisok[index_max], spisok[index_min] = spisok[index_min], spisok[index_max]
print(spisok)