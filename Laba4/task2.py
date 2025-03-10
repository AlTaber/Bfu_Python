d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
value = input()
for k, v in d.items():
    if (v == value): print(k)