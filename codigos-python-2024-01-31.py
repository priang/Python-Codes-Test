print(1)

print("Hello World!") #string
print('Hello World!') 

print(type(True))

# print(var + 5)

# no python não é preciso declarar uma variável
# quando você escreve a variável, o python já identifica o tipo dela


#its Case Sensitive
variavel = 2
Variavel = 7
print(variavel)
print(Variavel)

#printar 2 strings

nome = 'Pri'
print("E aí,",nome,", tudo na boa?")

# coletar
apelido = input()
print("Bom dia, my dear",apelido)

apelido = input("Oi:")
print("Bom dia, my dear",apelido)


a=1.0
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# int +-/* float = float
# int / int = float
x = 10
y = 2
print(x/y)

consumido=100
gorjeta=0.1
print(consumido+(consumido*gorjeta))


consumido = input("Consumido: R$ ")
consumido_float = round(float(consumido),2)
gorjeta = round(0.1 * consumido_float,2)

print("")
print("Valor cohgkdjfhgkjdfhgkjdfhgdkjfhk dkghkjdfhgjkdhfj ghkjdhfgkjhd jkfgjkdhjk hjkdfhgjkdfh kjghdfjkhgkjdfhgkjd hfnsumido: R$",consumido_float)


print("Gorjeta do garçom: R$",gorjeta)
print("Total da Nota: R$", consumido_float + gorjeta)

print("Valor consumido: R$",consumido_float)

