varsta = 0
inaltime = 0
sexul = ''
greutate = 0

validationData = False
greutateaIdeala = 0

while not validationData:
    while True:
        varsta = int(input("Introduceti varsta: "))
        if 20 < varsta < 120:
            break
        else:
            print("Ati introdus incorect varsta!")

    while True:
        inaltime = int(input("Introduceti inaltimea: "))
        if 150 < inaltime < 220:
            break
        else:
            print("Ati introdus incorect inaltimea!")

    while True:
        sexul = input("Introduceti sexul: ").upper()
        if sexul == 'M' or sexul == 'F':
            break
        else:
            print("Ati introdus incorect sexul!")

    while True:
        greutate = int(input("Introduceti greutatea: "))
        if 45 < greutate < 300:
            break
        else:
            print("Ati introdus incorect greutatea!")

if sexul == 'M':
    greutateaIdeala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
else:
    greutateaIdeala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

diferenta = greutateaIdeala - greutate
if diferenta > 0:
    print("Trebuie sa scadeti din masa cu ", -diferenta, " kg")
else:
    print(f"Trebuie sa puneti in masa cu ", diferenta, " kg")
