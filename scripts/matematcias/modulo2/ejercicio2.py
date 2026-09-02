import numpy as np
import matplotlib.pyplot as plt

# Rango de entrada
x = np.linspace(-6, 6, 400)

# Definición de ReLU
def relu(x):
    return np.maximum(0, x)

# Definición de sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

y_relu = relu(x)
y_sigmoid = sigmoid(x)

plt.figure()
plt.plot(x, y_relu, label='ReLU(x)')
plt.plot(x, y_sigmoid, label='sigmoide(x)')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funciones de activación: ReLU y sigmoide')
plt.grid(True)
plt.legend()
plt.ylim(-0.5, 1.5)
#plt.show()
plt.savefig('grafico.png')