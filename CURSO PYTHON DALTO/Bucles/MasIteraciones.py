
frutas = ["banana", "pera", "manzana", "uva"]

for fruta in frutas:
    if fruta == "manzana":
        continue                             # Al llegar al continue se salto lo que queda de la iteración
    print(f"Me gusta la {fruta}")