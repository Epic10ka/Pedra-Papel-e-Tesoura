from datetime import date
contador = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {c}: '))
    dif = date.today().year - ano
    if dif >=18:
        contador = contador + 1
if c-contador == 1:
    print(f'{c-contador} é menor de idade e {contador} são maiores de idade.')
elif contador == 1:
    print(f'{c-contador} são menores de idade e {contador} é menor de idade.')
elif contador:
    print(f'{c-contador} são menores de idade e {contador} são maiores de idade.')
print(f'Ao todo, deram inputs de {c} pessoas.')