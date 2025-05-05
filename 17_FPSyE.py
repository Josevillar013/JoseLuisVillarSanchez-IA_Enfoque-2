import numpy as np
import matplotlib.pyplot as plt

# Par�metros del sistema y del filtro
dt = 0.1  # Intervalo de tiempo
A = np.array([[1, dt], [0, 1]])  # Matriz de transici�n de estado
H = np.array([[1, 0]])  # Matriz de observaci�n
Q = np.array([[0.01, 0], [0, 0.01]])  # Covarianza del proceso (ruido del sistema)
R = np.array([[0.1]])  # Covarianza de la medici�n (ruido del sensor)

# Datos de posici�n observada
np.random.seed(0)
posicion_verdadera = [t + np.random.normal(0, 0.5) for t in np.arange(0, 10, dt)]

# Aplicaci�n del filtro de Kalman para suavizado
x = np.array([[posicion_verdadera[0]], [0]])  # Estado inicial
P = np.eye(2) * 0.1  # Estimaci�n inicial de la covarianza del estado
posicion_suavizada = [x[0, 0]]
for z in posicion_verdadera[1:]:
    # Predicci�n
    x_pred = np.dot(A, x)
    P_pred = np.dot(np.dot(A, P), A.T) + Q
    
    # Actualizaci�n (correcci�n)
    y = z - np.dot(H, x_pred)
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = np.dot(np.eye(2) - np.dot(K, H), P_pred)
    
    posicion_suavizada.append(x[0, 0])

# Graficar resultados
plt.plot(np.arange(0, 10, dt), posicion_verdadera, label='Posicion Verdadera', color='b')
plt.plot(np.arange(0, 10, dt), posicion_suavizada, label='Posicion Suavizada', color='r', linestyle='--')
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
plt.title('Suavizado de Datos con Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()
