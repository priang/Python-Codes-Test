a = 10
b = 2

try:
    # a tarefa
    c = a / b
    print(c)
except:
    # se der erro
    print('deu erro!')
else:
    #  quero executar caso não de erro
    print(c)
finally:
    # executa independentemente do resultado do try - executa sempre
    print("Continua o programa")

#  podemos especificar qual tipo de erro que podemos
#  python tem vários tipos de erros bulting
#  um deles é a divisão por zero

a = 10
b = "A"
try:
    # a tarefa
    c = a / b
    print(c)
except ZeroDivisionError:  # só vai executar se for um erro de divisão por zero
    # se der erro
    print('deu erro!')
else:
    #  quero executar caso não de erro
    print(c)
finally:
    # executa independentemente do resultado do try - executa sempre
    print("Continua o programa")
