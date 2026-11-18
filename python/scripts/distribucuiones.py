import numpy as np
import matplotlib.pyplot as plt
import math

# -----------------------------
# Funciones para cada distribución
# -----------------------------

def plot_bernoulli():
    """
    Distribución Bernoulli(p)
    Parámetro hardcodeado: p = 0.3
    """
    p = 0.3
    x = [0, 1]
    pmf = [1 - p, p]

    plt.figure()
    plt.bar(x, pmf)
    plt.xticks(x)
    plt.title(f"Distribución Bernoulli(p={p})")
    plt.xlabel("x")
    plt.ylabel("P(X=x)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    # plt.show()
    plt.savefig("bernoulli.png")


def plot_binomial():
    """
    Distribución Binomial(n, p)
    Parámetros hardcodeados: n = 10, p = 0.5
    """
    n = 10
    p = 0.5
    x = np.arange(0, n + 1)

    def binomial_pmf(k, n, p):
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    pmf = [binomial_pmf(k, n, p) for k in x]

    plt.figure()
    plt.bar(x, pmf)
    plt.title(f"Distribución Binomial(n={n}, p={p})")
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    #plt.show()
    plt.savefig("binomial.png")

def plot_poisson():
    """
    Distribución Poisson(λ)
    Parámetro hardcodeado: λ = 4
    """
    lam = 4
    # Rango de k centrado alrededor de λ
    x = np.arange(0, 15)

    def poisson_pmf(k, lam):
        return (lam ** k) * np.exp(-lam) / math.factorial(k)

    pmf = [poisson_pmf(k, lam) for k in x]

    plt.figure()
    plt.bar(x, pmf)
    plt.title(f"Distribución Poisson(λ={lam})")
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    #plt.show()
    plt.savefig("poisson.png")


def plot_uniform():
    """
    Distribución Uniforme continua U(a, b)
    Parámetros hardcodeados: a = 0, b = 1
    """
    a, b = 0, 1
    x = np.linspace(a - 0.2, b + 0.2, 400)
    f = np.where((x >= a) & (x <= b), 1 / (b - a), 0)

    plt.figure()
    plt.plot(x, f)
    plt.title(f"Distribución Uniforme(a={a}, b={b})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.ylim(0, max(f) * 1.2)
    plt.grid(True, linestyle="--", alpha=0.5)
    #plt.show()
    plt.savefig("uniforme.png")


def plot_normal():
    """
    Distribución Normal(μ, σ)
    Parámetros hardcodeados: μ = 0, σ = 1
    """
    mu, sigma = 0, 1
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
    f = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

    plt.figure()
    plt.plot(x, f)
    plt.title(f"Distribución Normal(μ={mu}, σ={sigma})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle="--", alpha=0.5)
    #plt.show()
    plt.savefig("normal.png")


def plot_exponential():
    """
    Distribución Exponencial(λ)
    Parámetro hardcodeado: λ = 0.5
    (media = 1/λ = 2)
    """
    lam = 0.5
    x = np.linspace(0, 15, 400)
    f = lam * np.exp(-lam * x)

    plt.figure()
    plt.plot(x, f)
    plt.title(f"Distribución Exponencial(λ={lam})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle="--", alpha=0.5)
    #plt.show()
    plt.savefig("exponencial.png")


# -----------------------------
# Menú interactivo
# -----------------------------

def mostrar_menu():
    print("\n--- Graficador de Distribuciones Fundamentales ---")
    print("1) Bernoulli")
    print("2) Binomial")
    print("3) Poisson")
    print("4) Uniforme")
    print("5) Normal")
    print("6) Exponencial")
    print("0) Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            plot_bernoulli()
        elif opcion == "2":
            plot_binomial()
        elif opcion == "3":
            plot_poisson()
        elif opcion == "4":
            plot_uniform()
        elif opcion == "5":
            plot_normal()
        elif opcion == "6":
            plot_exponential()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
