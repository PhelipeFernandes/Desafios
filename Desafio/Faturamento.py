sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
print(total)
psp = (67836.43*100)/180759.98
prj = (36678.66*100)/180759.98
pmg = (29229.88*100)/180759.98
pes = (27165.48*100)/180759.98
poutros = (19849.53*100)/180759.98
print('''O percentual do estado de SP é {:.2f} \n
O percentual do estado de RJ é {:.2f} % \n
O percentual do estado de MG é {:.2f} % \n
O percentual do estado de ES é {:.2f} % \n
O percentual dos estado restantes é {:.2f}%
'''.format(psp, prj, pmg, pes, poutros))