#EXERCÍCIO Nº 11 - LISTA 02 - ESTRUTURA DE DECISÃO
print('Reajuste de salários')
print('####################')

salário=float(input("Insira o valor total do seu salário: R$ "))

if salário<=280:
    print('Salário atual: R$ ',salário,';Reajuste: 20%',';Valor do reajuste: R$ ',salário*0.2,';Novo salário: R$ ',salário*1.2)
elif salário>280 and salário<=700:
    print('Salário atual: R$ ', salário,';Reajuste: 15%',';Valor do reajuste: R$ ', salário * 0.15,';Novo salário: R$ ',
          salário * 1.15)
elif salário>700 and salário<=1500:
    print('Salário atual: R$ ', salário,';Reajuste: 10%',';Valor do reajuste: R$ ', salário * 0.1,';Novo salário: R$ ',
          salário * 1.1)
else:
    print('Salário atual: R$ ', salário,';Reajuste: 5%',';Valor do reajuste: R$ ', salário * 0.05,';Novo salário: R$ ',
          salário * 1.05)

