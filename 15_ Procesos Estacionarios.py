import numpy as np
import matplotlib.pyplot as plt

# Par�metros del proceso
longitud = 1000

# Generaci�n del proceso estacionario de caminata aleatoria
tiempo = np.arange(longitud)
pasos = np.random.choice([-1, 1], size=longitud)
posicion = np.cumsum(pasos)

# Graficamos el proceso estacionario de caminata aleatoria
plt.plot(tiempo, posicion)
plt.xlabel('Tiempo')
plt.ylabel('Posici�n')
plt.title('Proceso Estacionario de Caminata Aleatoria')
plt.grid(True)
plt.show()
