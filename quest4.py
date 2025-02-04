import random

aleatorio = random.randint(1, 100)
numero = int(input('Digite um número: '))
if numero == aleatorio:
    print('Você acertou!!')
elif numero < aleatorio:
    print('O número esta abaixo do número escolhido!')
else:
    print('O valor esta acima do número escolhido!')