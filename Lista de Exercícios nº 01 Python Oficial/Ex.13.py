print('Cálculo do peso ideal para homens e mulheres')
print('############################################')

altura=float(input('Insira sua altura (metros): '))

sexo=input('Insira seu sexo M/F: ')

peso=float(input('Insira seu peso (kg): '))

peso_idealM=(72.7*altura)-58
peso_idealF=(62.1*altura)-44.7

if sexo == 'M':
    print('Seu peso ideal é de: ',peso_idealM,'kg')
else:
    print('Seu peso ideal é de: ',peso_idealF,'kg')

if sexo == 'M' and peso>peso_idealM:
    print('Você esta acima do peso')
elif sexo == 'M' and peso<peso_idealM:
    print('Você está abaixo do peso')
elif sexo== 'F' and  peso>peso_idealF:
    print('Você esta acima do peso')
elif sexo == 'F' and peso<peso_idealF:
    print('Você está abaixo do peso')
else:
    print('Parabéns você esta no seu peso ideal!!')



