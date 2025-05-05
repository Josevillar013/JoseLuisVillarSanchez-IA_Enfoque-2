import numpy as np

# Funci�n para calcular la cinem�tica inversa de un brazo rob�tico de 2 grados de libertad
def cinematica_inversa(x_objetivo, y_objetivo, l1, l2):
    # Calcular el �ngulo de la primera articulaci�n
    theta1 = np.arctan2(y_objetivo, x_objetivo)
    
    # Calcular la distancia desde la base del brazo hasta el punto objetivo
    distancia_objetivo = np.sqrt(x_objetivo**2 + y_objetivo**2)
    
    # Calcular el �ngulo de la segunda articulaci�n utilizando el teorema del coseno
    cos_theta2 = (l1**2 + l2**2 - distancia_objetivo**2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    # Devolver los �ngulos calculados en radianes
    return theta1, theta2

# Par�metros del brazo rob�tico
longitud_l1 = 1.5
longitud_l2 = 1.0
posicion_objetivo_x = 1.0
posicion_objetivo_y = 1.0

# Calcular los �ngulos de las articulaciones para alcanzar la posici�n objetivo
theta1, theta2 = cinematica_inversa(posicion_objetivo_x, posicion_objetivo_y, longitud_l1, longitud_l2)

# Mostrar los �ngulos calculados
print("Angulo de la primera articulacion:", np.degrees(theta1))
print("Angulo de la segunda articulacion:", np.degrees(theta2))
