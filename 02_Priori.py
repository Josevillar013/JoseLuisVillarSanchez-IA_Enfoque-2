# Probabilidad a priori de que un correo electrónico sea spam o no spam
probabilidad_no_spam = 0.7
probabilidad_spam = 0.3

# Función para predecir si un correo electrónico es spam o no
def predecir_spam(probabilidad):
    if probabilidad > 0.5:
        return "Spam"
    else:
        return "No Spam"

# Ejemplo de probabilidad a priori en acción
probabilidad_correo = 0.85  # Probabilidad calculada por el modelo
prediccion = predecir_spam(probabilidad_correo)

print(f"El modelo predice que el correo es: {prediccion}")
