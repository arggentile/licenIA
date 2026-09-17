def fusionar_listas(a, b):
    i = j = 0
    resultado = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado

lista1 = [2, 5, 8, 10 ,12]
lista2 = [1, 2, 3, 5, 7, 8, 9, 10]
print(f"Fusión: {fusionar_listas(lista1, lista2)}")