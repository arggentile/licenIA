import matplotlib.pyplot as plt
import numpy as np

# Épocas de entrenamiento
epochs = np.arange(1, 51)  # 1 a 50

# Simulación de pérdida: baja rápido al principio y luego se estabiliza
loss = 2.5 * np.exp(-epochs / 10) + 0.2  # modelo simple para ilustrar

plt.figure()
plt.plot(epochs, loss, marker='o')

plt.xlabel('Épocas de entrenamiento')
plt.ylabel('Pérdida')
plt.title('Evolución de la pérdida durante el entrenamiento')
plt.grid(True)
plt.savefig("actividad3png")
