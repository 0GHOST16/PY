produse = ["lapte", "paine", "oua"]
preturi = [5, 3, 10]

for i in range(len(produse)):
    mesaj = "Produsul: {} are prețul de {} lei".format(produse[i], preturi[i])
    print(mesaj)