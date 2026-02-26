from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

#ESTÉTICA
print('———'*18)
print('—='*27)
print('ESCOLHA: \033[1;31mPEDRA(0)\033[m, \033[1mPAPEL(1) ou \033[1;34mTESOURA(2)\033[m'.center(75))
print('—='*27)
#ESTÉTICA

#JOGADA
player_turn = int(input('JOGUE: '))
jogada_pc = itens[pc].upper()
jogada_player = itens[player_turn].upper()
print(f'Você escolheu: {jogada_player}')
from time import sleep
print('PEDRA')
sleep(0.6)
print('PAPEL')
sleep(0.6)
print('TESOU-')
sleep(0.8)
print('RA!')
print('———'*18)
print(f'\033[1;34mSUA JOGADA: {jogada_player}\033[m | \033[1;31mJOGADA DO PC: {jogada_pc}\033[m')
#JOGADA

print()

if jogada_player == jogada_pc:
    print('\033[1;93mEMPATE!\033[m'.center(50))
elif jogada_player == 'PAPEL' and jogada_pc == 'PEDRA' or jogada_player == 'PEDRA' and jogada_pc == 'TESOURA' or jogada_player == 'TESOURA' and jogada_pc == 'PAPEL':
    print('\033[1;94mVITÓRIA!\033[m'.center(50))
else:
    print('\033[1;91mDERROTA!\033[m'.center(50))
sleep(5)
