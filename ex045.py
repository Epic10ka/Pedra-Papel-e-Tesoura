print('—='*16)
print('\033[1mPedra, Papel & Tesoura\033[m'.center(39))
print('—='*16)
print()
print(' \033[1mPEDRA(0), PAPEL(1), TESOURA(2)\033[m')
print()
print('\033[1;31mVEREMOS\033[m se é \033[1mCAPAZ\033[m de \033[1;34mGANHAR\033[m de mim!')
print()
from random import randint
def jogar():
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

    #play do pc
    pc = randint(0, 2)
    jogada_pc = opcoes[pc]

    #jogada do player
    player = int(input('JOGUE!: '))
    p_player = opcoes[player]

    print(f'Sua jogada: {p_player} | Computador: {jogada_pc}')
    print()
    if p_player == 'PEDRA' and jogada_pc == 'PEDRA' or p_player == 'PAPEL' and jogada_pc == 'PAPEL' or p_player == 'TESOURA' and jogada_pc == 'TESOURA':
        print('\033[1;33mEMPATE!\033[m'.center(50))
    elif p_player == 'PAPEL' and jogada_pc == 'PEDRA' or p_player == 'TESOURA' and jogada_pc == 'PAPEL' or p_player == 'PEDRA' and jogada_pc == 'TESOURA':
        print('\033[1;32mVITÓRIA!\033[m'.center(50))
    else:
        print('\033[1;31mDERROTA!\033[m'.center(50))
jogar()

