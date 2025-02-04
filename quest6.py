numeros = []
cont_par = 0
cont_impar = 0
for x in range (1,11):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
for numero in numeros:
    if numero %2 == 0:
        cont_par = cont_par +1
    else:
        cont_impar = cont_impar +1
print('Quantidade de números pares: ', cont_par)
print('Quantidade de números pares: ', cont_impar)