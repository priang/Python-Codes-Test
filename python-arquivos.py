

# abrindo arquivo para leitura
# arquivo = open('teste.txt')
# ou
# arquivo2 = open('teste.txt','r')

#  abrindo arquivo para ESCRITA

arquivo3 = open('novo.txt','w')

a = arquivo3.write('banana')
print(a)

b = arquivo3.write('melancia')
print(b)

# fecha o arquivo
arquivo3.close()

# abre novamente, agora insere dados
arquivo3 = open('novo.txt','a')

arquivo3.write('morango\n')
arquivo3.write('manga\n')

arquivo3.close()

arquivo = open('novo.txt','r')

# a = arquivo.read()
# print(a)
# print(type(a))

print(arquivo.read())

arquivo.close()

arquivo = open('novo.txt', 'r')
n = 1
for linha in arquivo:
    print(f'linha {n} - {linha}')
    n += 1
arquivo.close()
# saída
# linha 1 - bananamelanciamorango
# 
# linha 2 - manga

# tem uma linha vazia entre as linhas, isso é por causa do print() que acrescenta esse \n

arquivo = open('novo.txt', 'r')
lista = []

for linha in arquivo:
    linha = linha.strip()
    lista.append(linha)

print(lista)
