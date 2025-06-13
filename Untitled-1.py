
# trabalhando com conjuntos, listas e dicionarios

conjunto1 = {1,0,3.5,"casa","d","e","f"}  #set
lista = ["a","b","c"]
dicionario = {"d":123,"e":234}

conjunto2 = set(dicionario) | set(lista)

# usar difference ou o operador '-' tera o mesmo resultado
# opcao 1
conjunto3 = conjunto1.difference(conjunto2)

# opcao 2
conjunto4 = conjunto1 - conjunto2

print('conjunto 3', conjunto3)
print('conjunto 4', conjunto4)
