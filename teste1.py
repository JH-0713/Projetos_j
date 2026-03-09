lista = ['1', '2', 'flamingo', '3', '4', '5', '6', '7', '8', '9']

for i in lista:
    if '1' in i:
        lista.pop(int(i))
    else:
        print(i)
