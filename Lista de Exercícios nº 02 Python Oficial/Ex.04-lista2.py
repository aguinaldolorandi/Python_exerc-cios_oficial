#EXERCÍCIO Nº 04 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Consoante ou vogal')
print('##################')

letra=input('Digite uma letra qualquer: ')


if len(letra)>1:
    print('OPÇÃO INVÁLIDA')
elif 'AEIOU'.find(letra.upper())>=0:
    print('VOGAL')
elif letra.isalpha():
    print('CONSOANTE')
else:
    print('OPÇÃO INVÁLIDA')
