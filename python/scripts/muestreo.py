import numpy as np
import matplotlib.pyplot as plt

def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

def leer_flotante(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número real.")


def mostrar_resultados_y_histograma(muestra, nombre_dist, discreta=False):
    media = np.mean(muestra)
    varianza = np.var(muestra)
    n = len(muestra)

    print("\n--- Resultados del muestreo ---")
    print(f"Distribución:         {nombre_dist}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Media aproximada:     {media:.5f}")
    print(f"Varianza aproximada:  {varianza:.5f}")
    print("Primeros 10 valores:", muestra[:10])
    print("-------------------------------\n")

    # Histograma
    plt.figure()
    if discreta:
        min_val = int(np.min(muestra))
        max_val = int(np.max(muestra))
        bins = np.arange(min_val - 0.5, max_val + 1.5, 1)
        plt.hist(muestra, bins=bins, edgecolor='black', rwidth=0.8)
    else:
        plt.hist(muestra, bins=20, edgecolor='black')

    plt.title(f"Histograma - {nombre_dist}")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle="--", alpha=0.4)

    # --- Caja con los resultados en la esquina superior derecha ---
    texto = (
        f"n = {n}\n"
        f"media = {media:.4f}\n"
        f"varianza = {varianza:.4f}"
    )
    plt.gca().text(
        0.98, 0.97, texto,
        transform=plt.gca().transAxes,   # coordenadas 0–1 relativas al eje
        ha='right', va='top',
        fontsize=10, family='monospace',
        bbox=dict(boxstyle='round,pad=0.4',
                  facecolor='white',
                  edgecolor='gray',
                  alpha=0.9)
    )

    plt.savefig(nombre_dist + ".png", bbox_inches='tight', dpi=120)
    plt.close()
    
def mostrar_resultados_y_histogramas(muestra, nombre_dist, discreta=False):
    print("\n--- Resultados del muestreo ---")
    print(f"Distribución:          {nombre_dist}")
    print(f"Tamaño de la muestra: {len(muestra)}")
    print(f"Media aproximada:     {np.mean(muestra):.5f}")
    print(f"Varianza aproximada:  {np.var(muestra):.5f}")
    print("Primeros 10 valores:", muestra[:10])
    print("-------------------------------\n")

    # Histograma
    plt.figure()
    if discreta:
        # Bins centrados en los enteros
        min_val = int(np.min(muestra))
        max_val = int(np.max(muestra))
        bins = np.arange(min_val - 0.5, max_val + 1.5, 1)
        plt.hist(muestra, bins=bins, edgecolor='black', rwidth=0.8)
    else:
        plt.hist(muestra, bins=20, edgecolor='black')

    plt.title(f"Histograma - {nombre_dist}")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle="--", alpha=0.4)
    #plt.show()
    plt.savefig(nombre_dist + ".png")

def muestrear_bernoulli():
    print("\n--- Distribución Bernoulli ---")
    p = leer_flotante("Ingrese p (probabilidad de éxito, entre 0 y 1): ", 0.0, 1.0)
    n = leer_entero("Ingrese el tamaño de la muestra: ", 1)
    muestra = np.random.binomial(1, p, size=n)
    mostrar_resultados_y_histograma(muestra, "Bernoulli", discreta=True)

def muestrear_binomial():
    print("\n--- Distribución Binomial ---")
    n_ensayos = leer_entero("Ingrese n (cantidad de ensayos por experimento, n >= 1): ", 1)
    p = leer_flotante("Ingrese p (probabilidad de éxito en cada ensayo, entre 0 y 1): ", 0.0, 1.0)
    n = leer_entero("Ingrese el tamaño de la muestra (cantidad de experimentos): ", 1)
    muestra = np.random.binomial(n_ensayos, p, size=n)
    mostrar_resultados_y_histograma(muestra, "Binomial", discreta=True)

def muestrear_poisson():
    print("\n--- Distribución Poisson ---")
    lam = leer_flotante("Ingrese lambda (tasa de eventos, > 0): ", 0.0)
    n = leer_entero("Ingrese el tamaño de la muestra: ", 1)
    muestra = np.random.poisson(lam=lam, size=n)
    mostrar_resultados_y_histograma(muestra, "Poisson", discreta=True)

def muestrear_uniforme():
    print("\n--- Distribución Uniforme ---")
    a = leer_flotante("Ingrese el límite inferior a: ")
    b = leer_flotante("Ingrese el límite superior b (b > a): ")
    while b <= a:
        print("Error: se requiere b > a.")
        b = leer_flotante("Ingrese el límite superior b (b > a): ")
    n = leer_entero("Ingrese el tamaño de la muestra: ", 1)
    muestra = np.random.uniform(a, b, size=n)
    mostrar_resultados_y_histograma(muestra, "Uniforme", discreta=False)

def muestrear_normal():
    print("\n--- Distribución Normal (Gaussiana) ---")
    mu = leer_flotante("Ingrese la media (mu): ")
    sigma = leer_flotante("Ingrese la desviación estándar (sigma > 0): ", 0.0)
    while sigma <= 0:
        print("sigma debe ser > 0.")
        sigma = leer_flotante("Ingrese la desviación estándar (sigma > 0): ", 0.0)
    n = leer_entero("Ingrese el tamaño de la muestra: ", 1)
    muestra = np.random.normal(loc=mu, scale=sigma, size=n)
    mostrar_resultados_y_histograma(muestra, "Normal", discreta=False)

def muestrear_exponencial():
    print("\n--- Distribución Exponencial ---")
    lam = leer_flotante("Ingrese lambda (> 0): ", 0.0)
    while lam <= 0:
        print("lambda debe ser > 0.")
        lam = leer_flotante("Ingrese lambda (> 0): ", 0.0)
    n = leer_entero("Ingrese el tamaño de la muestra: ", 1)
    # en NumPy, scale = 1/lambda
    muestra = np.random.exponential(scale=1.0/lam, size=n)
    mostrar_resultados_y_histograma(muestra, "Exponencial", discreta=False)

def mostrar_menu():
    print("=======================================")
    print("  Muestreo desde distribuciones clásicas")
    print("=======================================")
    print("1) Bernoulli")
    print("2) Binomial")
    print("3) Poisson")
    print("4) Uniforme")
    print("5) Normal (Gaussiana)")
    print("6) Exponencial")
    print("0) Salir")
    print("=======================================")

def main():
    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ", 0, 6)

        if opcion == 0:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            muestrear_bernoulli()
        elif opcion == 2:
            muestrear_binomial()
        elif opcion == 3:
            muestrear_poisson()
        elif opcion == 4:
            muestrear_uniforme()
        elif opcion == 5:
            muestrear_normal()
        elif opcion == 6:
            muestrear_exponencial()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
