import numpy as np

# NumPy é amplamente utilizado em computação científica porque grande parte de sua implementação interna
# é feita em C, o que garante alta performance na execução de operações matemáticas e manipulação de arrays.
# Apesar disso, sua interface é acessada por meio de código Python, permitindo facilidade de uso.

a1 = np.array([1, 2, 3])

print(a1)
print(type(a1)) # perceba que não é array ou list, mas sim, 'numpy.ndarray'

a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a2)
print(type(a2))

# Analisando linhas (unidimensional - bidimensional - tridimensional)

print(a1.shape) # unidimensional
print(a2.shape) # bidimensional