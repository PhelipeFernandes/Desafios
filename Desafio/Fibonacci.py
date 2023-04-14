termos = int(input('Quantos termos você deseja mostrar? '))
incluso = str(input('Qual numero você deseja encontrar? '))
n1 = 0
n2 = 1
c = 3
print('{} -> {}'.format(n1, n2), end='')
while c <= termos:
    n3 = n1 + n2
    print(" -> {}".format(n3), end='')
    n1 = n2
    n2 = n3
    c += 1
print(' -> FIM')

#A partir daqui não consegui prosseguir.


