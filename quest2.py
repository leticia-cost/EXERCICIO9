contador = 0
frase = input('Digite uma frase: ')
for x in frase:
    if x in list('aeiou') or list('AEIOU'):
        contador = contador + 1

print('Quantidade de vogais: ',contador)