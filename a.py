# 1. Crie um set de 10 números inteiros aleatórios usando um loop.
import random

set1 = set()

for elem in range(10):
    a = random.randint(1, 100)
    set1.add(a)

print(set1)

# 2. Remova todos os números pares do set criado no item anterior e crie um novo set com esses números removidos.
nr_impares = set()
for elem in set1.copy():
    if (elem % 2 == 0):  # se for par
        set1.remove(elem)
        nr_impares.add(elem)

print('ex2 - set', set1)
print('ex2 - set nr_impares', nr_impares)

# 3. Remova o maior número do set criado no item 2.
maior = max(nr_impares)
nr_impares.remove(maior)

print('ex3 - set nr_impares', nr_impares)

# 4. Adicione o dobro do maior número do set do item 1 no set do item 2.
maior_set1 = 2 * max(set1)
nr_impares.add(maior_set1)

print('ex4 - maior set1', maior_set1)
print('ex4 - set nr_impares', nr_impares)

'''
5. Dados os sets: S1 = set(range(5)) e S2 = set(range(3:9)), escreva um programa que mostre:
A união de S1 e S2
A intersecção de S1 e S2
A diferença entre S1 e S2
A diferença entre S2 e S1
A diferença simétrica entre S1 e S2
Um subset do item a
'''

s1 = set(range(5))
s2 = set(range(3, 9))

# A união de S1 e S2
print('s1', s1)
print('s2', s2)
print('união', s1 | s2)
print('intersecção', s1 & s2)
print('diferença s1/s2', s1 - s2)
print('diferença s2/s1', s2 - s1)
print('diferença simétrica s1/s2', s1 ^ s2)

subsetA = {1, 4, 9}
A = s1 | s2
print('subset', A.issubset(subsetA))
