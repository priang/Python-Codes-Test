
set1 = {1,0,3.5,"casa","d","e","f"}
lista = ["a","b","c"]
dicionario = {"d":123,"e":234}

set2 = set(dicionario) | set(lista)

set4 = set1.difference(set2)
#ou (tem a mesma funcao)
set4 = set1 - set2

print(set4)