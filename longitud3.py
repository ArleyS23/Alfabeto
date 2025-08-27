from itertools import product

# Definir alfabeto y longitud máxima
alfabeto = ['0', '1']
longitud_max = 3

# Generar lenguaje
L = set()

for i in range(1, longitud_max + 1):
    for p in product(alfabeto, repeat=i):
        L.add("".join(p))

# Mostrar resultado
print("Lenguaje L con Σ={0,1} y longitud ≤ 3:")
print(L)
