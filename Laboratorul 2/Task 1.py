fructe = ["mar", "banana", "portocala", "pere"]

print("1 valoare:", fructe[0])
print("3 valoare:", fructe[2])

fructe[1] = "piersic"
print("Lista noua:", fructe)

sublista = fructe[1:3]
print("Lista:", sublista)

fructe.append("gutuie")
print("Lista:", fructe)

print("Lungimea listei:", len(fructe))
print("Lista sortata", sorted(fructe))

fructe_noi = fructe + ["kiwi", "ananas"]
print("Lista dupa concatenare:", fructe_noi)

del fructe[1]
print("Listă după stergerea elementului 1:", fructe)

print("Primul element:", fructe[0])