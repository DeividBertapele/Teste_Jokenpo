#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

# definit os itens

itens = ('Pedra', 'Papel', 'Tesoura')

# jogada do computador

computador = randint(0, 2)

#vamos printar as opções
print('{:=^50}'.format('JOKENPÔ'))

print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')

print('=='*15)

jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(2)

print('-='*15)

print('Computador jogou {}'.format(itens[computador]))
print('-='*15)

print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)

if computador == 0:   # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!!')

elif computador == 1:     # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!!')

elif computador == 2:      #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!!')
