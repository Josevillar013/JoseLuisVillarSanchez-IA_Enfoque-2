# Definimos una frase para analizar
sentence = "the cat chased the bird on the roof"

# Creamos un parser probabil�stico basado en la gram�tica
parser = nltk.ViterbiParser(grammar)

# Analizamos la frase y mostramos los �rboles de an�lisis m�s probables
for tree in parser.parse(sentence.split()):
    print("Arbol de Analisis:")
    print(tree)
    print("Probabilidad:", parser.probability(tree))
