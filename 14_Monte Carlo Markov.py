import numpy as np
import matplotlib.pyplot as plt

# Definimos la funci�n de densidad de probabilidad de la distribuci�n objetivo (normal)
def pdf_objetivo(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Funci�n de propuesta: distribuci�n normal sim�trica alrededor del valor actual
def propuesta(x_actual):
    return np.random.normal(x_actual, 0.5)

# Algoritmo Metropolis-Hastings
def metropolis_hastings(iteraciones):
    muestras = []
    x_actual = np.random.normal(0, 1)  # Estado inicial
    for _ in range(iteraciones):
        x_propuesto = propuesta(x_actual)
        aceptacion = min(1, pdf_objetivo(x_propuesto) / pdf_objetivo(x_actual))
        if np.random.rand() < aceptacion:
            x_actual = x_propuesto
        muestras.append(x_actual)
    return muestras

# Generamos muestras con el algoritmo Metropolis-Hastings
muestras = metropolis_hastings(10000)

# Graficamos las muestras junto con la distribuci�n objetivo
plt.hist(muestras, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(-3, 3, 100)
plt.plot(x, pdf_objetivo(x), color='r', linestyle='--', linewidth=2)
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Muestreo de una Distribuci�n Normal con Metropolis-Hastings')
plt.grid(True)
plt.show()
