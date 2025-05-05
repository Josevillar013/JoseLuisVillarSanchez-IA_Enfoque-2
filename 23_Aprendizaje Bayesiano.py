import numpy as np
import pymc3 as pm

# Datos observados
datos = np.random.normal(loc=5, scale=2, size=100)

# Definici�n del modelo bayesiano
with pm.Model() as modelo:
    # Par�metros
    mu = pm.Normal('mu', mu=0, sigma=10)   # Media de la distribuci�n normal
    sigma = pm.HalfNormal('sigma', sigma=1)  # Desviaci�n est�ndar positiva de la distribuci�n normal
    
    # Likelihood
    observaciones = pm.Normal('observaciones', mu=mu, sigma=sigma, observed=datos)
    
    # Inferencia
    traza = pm.sample(1000, tune=1000)

# Resultados
pm.summary(traza)
pm.traceplot(traza)
