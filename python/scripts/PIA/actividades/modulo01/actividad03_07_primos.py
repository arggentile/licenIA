def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: #divisivle por 2
        return False
    for i in range(3, n - 1): # se puede mejorar optmizando la division
        if n % i == 0:
            return False
    return True



def main():
    while True:
        numero = input("Ingrese un número entero positivo: ")
        numero = int(numero)
        if numero > 0:
            primos = [n for n in range(2, numero - 1) if es_primo(n)]
            if primos:
                print(f"\nNúmeros primos menores o iguales a {numero}:")
                print(", ".join(map(str, primos)))
                print(f"\nTotal: {len(primos)} número(s) primo(s).")
            else:
                print(f"\nNo hay números primos menores o iguales a {numero}.")
        elif numero == 0:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()