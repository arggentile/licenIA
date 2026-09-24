def emparejar_listas(a, b):
    i = j = 0
    resultado = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            resultado.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return resultado

lista1 = [2, 5, 8, 10 ,12]
lista2 = [1, 2, 3, 5, 7, 8, 9, 10]
print(f"Emparejamiento: {emparejar_listas(lista1, lista2)}")