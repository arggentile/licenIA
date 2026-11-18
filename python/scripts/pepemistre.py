import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parámetros
lam_hat = 1.5
n = 600
se = np.sqrt(lam_hat / n)        # 0.05
z = 1.96
ic_low, ic_high = lam_hat - z*se, lam_hat + z*se

# Curva Normal del estimador
x = np.linspace(lam_hat - 4*se, lam_hat + 4*se, 400)
y = stats.norm.pdf(x, lam_hat, se)

# Gráfico
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='#2563EB', linewidth=2)

# Zona sombreada del 95 %
mask = (x >= ic_low) & (x <= ic_high)
ax.fill_between(x, 0, y, where=mask, alpha=0.3,
                color='#2563EB', label='95 % de confianza')

# Líneas verticales
ax.axvline(lam_hat, color='black', linestyle='--',
           linewidth=1.5, label=f'λ̂ = {lam_hat}')
ax.axvline(ic_low, color='red', linestyle=':',
           linewidth=1.5, label=f'Lím. inf. = {ic_low:.2f}')
ax.axvline(ic_high, color='red', linestyle=':',
           linewidth=1.5, label=f'Lím. sup. = {ic_high:.2f}')

# Etiquetas
ax.set_title('Intervalo de confianza del 95 % para λ',
             fontsize=14)
ax.set_xlabel('Valor de λ', fontsize=12)
ax.set_ylabel('Densidad', fontsize=12)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("ssss.png")
