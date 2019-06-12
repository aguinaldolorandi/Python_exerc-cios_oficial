# EXERCÍCIO Nº 14- LISTA 06 - STRINGS
print('\nLEET SPEEK GENERATOR')
print('####################\n')

leet = {
    'A': '4',
    'B': '8',
    'C': '<',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2',
    ' ': ' '
}

texto = input('Insira um texto para traduzir:').upper()
if texto.isalpha():
    print('\nO texto traduzido é: ',end='')
    for letra in texto:
        print(leet[letra],end='')
else:
    print('Digite apenas texto')