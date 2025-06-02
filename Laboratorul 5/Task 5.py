lista = [1, 2, 3, 4, 3, 2, 3]
dictionar = {'a': 3, 'b': 2, 'c': 3}
text = "abra cadabra"

valoare = 3
contor = 0

for elem in lista:
    if elem == valoare:
        contor += 1

for val in dictionar.values():
    if val == valoare:
        contor += 1

for char in text:
    if char == 'a':
        contor += 1

print("Valoarea apare de",  contor, "ori.")