nomes =[]
cont = 0
for x in range (5):
    nome = input('Digite um nome: ')
    nomes.append(nome)
    if nome[0] == 'A' or nome[0] == 'a':
        cont += 1
print('Quantidade de nomes que iniciam com "A": ', cont)