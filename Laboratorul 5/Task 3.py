lista = [1, 3, 5, 3, 7, 3, 9]
dictionar = {'a': 3, 'b': 5, 'c': 3, 'd': 8}
text = "Mesaj1_Mesaj"

valoare_cautata = 3
caracter_cautat = 'a'

contor_lista = 0
contor_dict = 0
contor_text = 0

for elem in lista:
    if elem == valoare_cautata:
        contor_lista += 1

for val in dictionar.values():
    if val == valoare_cautata:
        contor_dict += 1

for char in text:
    if char == caracter_cautat:
        contor_text += 1

print("Valoarea", valoare_cautata, "apare de", contor_lista, "ori în lista")
print("Valoarea", valoare_cautata, "apare de", contor_dict, "ori în dicționar")
print("Caracterul", caracter_cautat, "apare de", contor_text, "ori în text")
