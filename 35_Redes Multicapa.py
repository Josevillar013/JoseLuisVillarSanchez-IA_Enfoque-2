# Importamos las bibliotecas necesarias
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Definimos la arquitectura de la red neuronal
modelo = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Capa de entrada: aplanamos la imagen de 28x28 a un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Primera capa oculta con 128 neuronas y activación ReLU
    layers.Dense(64, activation='relu'),   # Segunda capa oculta con 64 neuronas y activación ReLU
    layers.Dense(10, activation='softmax') # Capa de salida con 10 neuronas (una para cada clase) y activación softmax
])

# Compilamos el modelo
modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Cargamos y preprocesamos los datos de MNIST
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = keras.datasets.mnist.load_data()
x_entrenamiento, x_prueba = x_entrenamiento / 255.0, x_prueba / 255.0

# Entrenamos el modelo
modelo.fit(x_entrenamiento, y_entrenamiento, epochs=5)

# Evaluamos el modelo
puntuacion = modelo.evaluate(x_prueba,  y_prueba)
print("Precision en prueba:", puntuacion[1])
