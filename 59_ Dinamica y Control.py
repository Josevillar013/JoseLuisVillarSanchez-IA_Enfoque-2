import numpy as np
import matplotlib.pyplot as plt

# Funci�n para simular el movimiento del robot
def mover_robot(velocidad, dt):
    # Modelo de movimiento simple: el robot avanza a una velocidad constante
    nueva_posicion = velocidad * dt
    return nueva_posicion

# Funci�n para el control de velocidad proporcional
def control_velocidad(objetivo, actual, kp):
    # Calculamos la se�al de control proporcional
    se�al_control = kp * (objetivo - actual)
    return se�al_control

# Par�metros del controlador
kp = 0.5  # Ganancia proporcional

# Par�metros de simulaci�n
velocidad_objetivo = 1.0  # Velocidad deseada
tiempo_simulacion = 10.0  # Tiempo de simulaci�n en segundos
dt = 0.1  # Paso de tiempo

# Inicializamos el controlador y el estado del robot
velocidad_actual = 0.0  # Velocidad inicial del robot
tiempo = np.arange(0, tiempo_simulacion, dt)
posiciones = []

# Simulamos el control de velocidad y el movimiento del robot
for t in tiempo:
    se�al_control = control_velocidad(velocidad_objetivo, velocidad_actual, kp)
    velocidad_actual += se�al_control * dt
    nueva_posicion = mover_robot(velocidad_actual, dt)
    posiciones.append(nueva_posicion)

# Visualizamos los resultados
plt.plot(tiempo, posiciones)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posicion del Robot')
plt.title('Control de Velocidad Proporcional para un Robot Movil')
plt.grid(True)
plt.show()
