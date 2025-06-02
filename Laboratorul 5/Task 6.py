shopping_list = []

def adauga_produs(prod):
    if prod in shopping_list:
        print("Produsul", prod,  "este deja.")
    else:
        shopping_list.append(prod)
        print(f"Produsul '{prod}' a fost adăugat.")

def sterge_produs_dupa_nume(nume):
    if nume in shopping_list:
        shopping_list.remove(nume)
        print(f"Produsul '{nume}' a fost șters.")
    else:
        print(f"Produsul '{nume}' nu se află în listă.")

def sterge_produs_dupa_index(index):
    if index < 1 or index > len(shopping_list):
        print("Index invalid!")
    else:
        produs = shopping_list.pop(index - 1)
        print(f"Produsul '{produs}' a fost șters de la poziția {index}.")

def afiseaza_lista():
    if not shopping_list:
        print("Lista de cumpărături este goală.")
    else:
        for i, produs in enumerate(shopping_list, start=1):
            print(f"{i}. {produs}")

while True:
    print("\nMeniu:")
    print("1. Afișare listă")
    print("2. Adăugare produs")
    print("3. Ștergere produs")
    print("4. Ieșire")
    
    optiune = input("Selectează opțiunea (1-4): ")

    if optiune == "1":
        fn.afiseaza_lista()
    elif optiune == "2":
        produs = input("Introdu denumirea produsului: ")
        fn.adauga_produs(produs)
    elif optiune == "3":
        metoda = input("Ștergere după (n)ume sau (p)oziție? ")
        if metoda == "n":
            nume = input("Introdu denumirea: ")
            fn.sterge_produs_dupa_nume(nume)
        elif metoda == "p":
            poz = input("Introdu poziția produsului: ")
            if poz.isdigit():
                poz = int(poz)
                fn.sterge_produs_dupa_index(poz)
            else:
                print("Poziția trebuie să fie un număr pozitiv.")
        else:
            print("Opțiune invalidă de ștergere.")
    elif optiune == "4":
        print("Ieșire...")
        break
    else:
        print("Opțiune invalidă. Alege 1-4.")