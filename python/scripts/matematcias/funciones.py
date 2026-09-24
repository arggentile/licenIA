# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# ==== Definición de funciones matemáticas ==== #

def f_lineal(x, a=1.0, b=0.0):
    """Función afín: f(x) = a x + b"""
    return a * x + b

def f_polinomica(x):
    """Ejemplo de función polinómica: p(x) = 2x^2 - 3x + 1"""
    return 2 * x**2 - 3 * x + 1

def f_exponencial(x):
    """Función exponencial: f(x) = e^x"""
    return np.exp(x)

def f_logaritmica(x):
    """Función logarítmica natural: f(x) = ln(x) (dominio x > 0)"""
    return np.log(x)

def f_sigmoide(x):
    """Función sigmoide logística: σ(x) = 1 / (1 + e^{-x})"""
    return 1 / (1 + np.exp(-x))

def f_tanh(x):
    """Función tangente hiperbólica"""
    return np.tanh(x)

def f_relu(x):
    """Función ReLU: max(0, x)"""
    return np.maximum(0, x)


# ==== Rutinas de graficación ==== #

def graficar(x, y, titulo, xlabel="x", ylabel="f(x)"):
    """Función auxiliar para graficar con formato básico."""
    plt.figure()
    plt.plot(x, y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle="--", linewidth=0.5)
    nombre_png = "graficofuncion.png"
    plt.savefig(nombre_png)
    #plt.show()


# ==== Menú de opciones ==== #

def mostrar_menu():
    print("\n=== Menú de funciones ===")
    print("1) Función lineal / afín")
    print("2) Función polinómica")
    print("3) Función exponencial")
    print("4) Función logarítmica")
    print("5) Función sigmoide (logística)")
    print("6) Función tangente hiperbólica (tanh)")
    print("7) Función ReLU")
    print("0) Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break

        elif opcion == "1":
            # Permitir al usuario elegir parámetros a y b
            try:
                a = float(input("Ingrese el valor de a (pendiente) [ej: 1]: ") or 1)
                b = float(input("Ingrese el valor de b (ordenada al origen) [ej: 0]: ") or 0)
            except ValueError:
                print("Valores no válidos, se usarán a=1, b=0.")
                a, b = 1.0, 0.0

            x = np.linspace(-10, 10, 400)
            y = f_lineal(x, a, b)
            graficar(y=y, x=x, titulo=f"Función lineal / afín: f(x) = {a}x + {b}")

        elif opcion == "2":
            x = np.linspace(-5, 5, 400)
            y = f_polinomica(x)
            graficar(x, y, "Función polinómica: p(x) = 2x² - 3x + 1")

        elif opcion == "3":
            x = np.linspace(-2, 2, 400)
            y = f_exponencial(x)
            graficar(x, y, "Función exponencial: f(x) = e^x")

        elif opcion == "4":
            # Dominio positivo para el logaritmo
            x = np.linspace(0.01, 10, 400)
            y = f_logaritmica(x)
            graficar(x, y, "Función logarítmica: f(x) = ln(x)")

        elif opcion == "5":
            x = np.linspace(-10, 10, 400)
            y = f_sigmoide(x)
            graficar(x, y, "Función sigmoide logística: σ(x) = 1 / (1 + e^{-x})")

        elif opcion == "6":
            x = np.linspace(-10, 10, 400)
            y = f_tanh(x)
            graficar(x, y, "Función tangente hiperbólica: tanh(x)")

        elif opcion == "7":
            x = np.linspace(-10, 10, 400)
            y = f_relu(x)
            graficar(x, y, "Función ReLU: max(0, x)")

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()

