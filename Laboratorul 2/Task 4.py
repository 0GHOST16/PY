produse = {
    "mar": 5,
    "banana": 3,
    "portocala": 4
}

coduri = {
    101: "Pix",
    102: "Creion",
    103: "Caiet"
}

print("Pretul unui mar este:", produse["mar"])
print("Pretul unei portocale este:", produse["portocala"])

print("Cod 101 reprezinta:", coduri[101])
print("Cod 103 reprezinta:", coduri[103])

print("Pretul pentru gutuie (cu .get()):", produse.get("gutuie", "nu exista"))
produse.update({"banana": 4})
print("Dictionarul produse actualizat:", produse)

print("Numarul de produse:", len(produse))
print("Cheile din coduri ca lista:", list(coduri.keys()))