from hmmlearn import hmm
import numpy as np

# Definici�n del modelo HMM
modelo_hmm = hmm.GaussianHMM(n_components=2, covariance_type="full")

# Datos de entrada (secuencia de observaciones)
observaciones = np.array([[1.1], [0.9], [0.8], [1.0]])

# Entrenamiento del modelo
modelo_hmm.fit(observaciones)

# Generaci�n de la secuencia de estados ocultos
estados_ocultos = modelo_hmm.predict(observaciones)

# Predicci�n de la secuencia de observaciones
nuevas_observaciones, _ = modelo_hmm.sample(4)

print("Secuencia de estados ocultos predicha:", estados_ocultos)
print("Nuevas observaciones generadas:", nuevas_observaciones)
