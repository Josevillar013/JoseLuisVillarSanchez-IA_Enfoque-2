# Definimos una gram�tica probabil�stica lexicalizada para la generaci�n de frases
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V [0.3]
    NP -> Det N [0.6] | Det N PP [0.4]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.4] | 'dog' [0.4] | 'bird' [0.2]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Generamos frases probabil�sticamente utilizando la gram�tica
generated_trees = grammar.generate(5)

# Mostramos los �rboles de an�lisis generados
for tree in generated_trees:
    print("Arbol de Generacion:")
    print(tree)
