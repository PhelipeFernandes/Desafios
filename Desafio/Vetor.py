#Calcular faturamento
dia1 = float(input('Digite o faturamento do primeiro dia: '))
dia2 = float(input('Digite o faturamento do segundo dia: '))
dia3 = float(input('Digite o faturamento do terceiro dia: '))
dia4 = float(input('Digite o faturamento do quarto dia: '))
dia5 = float(input('Digite o faturamento do quinto dia: '))
dia6 = float(input('Digite o faturamento do sexto dia: '))
dia7 = float(input('Digite o faturamento do setimo dia: '))

maior = dia1

if dia2 > dia3 and dia2 > dia4 and dia2 > dia5 and dia2 > dia6 and dia2 > dia7:
    print('O maior faturamento foi o de R${:.2f}'. format(dia2))
if dia3 > dia2 and dia3 > dia4 and dia3 > dia5 and dia3 > dia6 and dia3 > dia7:
    print('O maior faturamento foi o de R${:.2f}'. format(dia3))
if dia4 > dia2 and dia4 > dia3 and dia4 > dia5 and dia4 > dia6 and dia4 > dia7:
    print('O maior faturamento foi o de R${:.2f}'. format(dia4))
if dia5 > dia2 and dia5 > dia3 and dia5 > dia4 and dia5 > dia6 and dia2 > dia7:
    print('O maior faturamento foi o de R${:.2f}'. format(dia5))
if dia6 > dia2 and dia6 > dia3 and dia6 > dia4 and dia6 > dia5 and dia6 > dia7:
    print('O maior faturamento foi o de R${:.2f}'. format(dia6))
if dia7 > dia2 and dia7 > dia3 and dia7 > dia4 and dia7 > dia5 and dia7 > dia6:
    print('O maior faturamento foi o de R${:.2f}'. format(dia7))

menor = dia1

if dia2 < dia3 and dia2 < dia4 and dia2 < dia5 and dia2 < dia6 and dia2 < dia7:
    print('O menor faturamento foi o de R${:.2F}'. format(dia2))
if dia3 < dia2 and dia3 < dia4 and dia3 < dia5 and dia3 < dia6 and dia3 < dia7:
    print('O menor faturamento foi o de R${:.2f}'. format(dia3))
if dia4 < dia2 and dia4 < dia3 and dia4 < dia5 and dia4 < dia6 and dia4 < dia7:
    print('O menor faturamento foi o de R${:.2f}'. format(dia4))
if dia5 < dia2 and dia5 < dia3 and dia5 < dia4 and dia5 < dia6 and dia2 < dia7:
    print('O menor faturamento foi o de R${:.2f}'. format(dia5))
if dia6 < dia2 and dia6 < dia3 and dia6 < dia4 and dia6 < dia5 and dia6 < dia7:
    print('O menor faturamento foi o de R${:.2f}'. format(dia6))
if dia7 < dia2 and dia7 < dia3 and dia7 < dia4 and dia7 < dia5 and dia7 < dia6:
    print('O menor faturamento foi o de R${:.2f}'. format(dia7))

media = (dia1 + dia2 + dia3 + dia4 + dia5 + dia6 + dia7) / 7
print('A média de vendas foi {:.2f}'.format(media))

if media < dia1:
    print('O primeiro dia de faturamento foi maior que a média. ')
if media < dia2:
    print('O segundo dia de faturamento foi maior que a média. ')
if media < dia3:
    print('O terceiro dia de faturamento foi maior que a média. ')
if media < dia4:
    print('O quarto dia de faturamento foi maior que a média. ')
if media < dia5:
    print('O quinto dia de faturamento foi maior que a média. ')
if media < dia6:
    print('O sexto dia de faturamento foi maior que a média. ')
if media < dia7:
    print('O sétimo dia de faturamento foi maior que a média. ')
