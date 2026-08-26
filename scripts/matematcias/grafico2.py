import numpy as np
import matplotlib.pyplot as plt

# Rango de valores para el parámetro w
w = np.linspace(-2, 8, 400)

# Función de pérdida (en forma de U)
L = (w - 3)**2 + 2

# Crear figura
plt.figure()
plt.plot(w, L, label='L(w) = (w - 3)^2 + 2')

# Marcar el mínimo
w_min = 3
L_min = (w_min - 3)**2 + 2
plt.scatter([w_min], [L_min])
plt.text(w_min, L_min + 0.5, 'mínimo', ha='center')

# Etiquetas
plt.xlabel('Parámetro w')
plt.ylabel('Pérdida L(w)')
plt.title('Función de pérdida en función del parámetro w')
plt.grid(True)
#plt.show()
plt.savefig('grafico2.png')
