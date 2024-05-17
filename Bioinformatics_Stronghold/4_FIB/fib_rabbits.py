#!/usr/bin/env python3

import sys
file = sys.argv[1]

with open(file,'r') as file:
	conteudo = file.read().strip().split()
	n = int(conteudo[0])
	k = int(conteudo[1])

geracoes = [0,1]

for mes in range(2,n+1):
	nova_geracao = geracoes[mes-1] + geracoes[mes-2]*k
	geracoes.append(nova_geracao)

print(geracoes[n])
#----------------------------------
print("="*58)
geracao_anterior = 1
geracao_ante_anterior = 0
for mes in range(2,n+1):
	geracao_n = geracao_anterior + geracao_ante_anterior*k
	geracao_ante_anterior = geracao_anterior
	geracao_anterior = geracao_n
print(geracao_n)
#----------------------------------
print("="*58)
a = 0
b = 1

for mes in range(2,n+1):
	a_temp = a
	a = a+b
	b = a_temp*k

print(a+b)



#geracao_anterior = 1
#geracao_ante_anterior = 0
for mes in range(n):
	if mes == 0:
		geracao_ante_anterior = 0
		geracao_anterior = 1
	else:
		geracao_n = geracao_anterior + geracao_ante_anterior*k
		geracao_ante_anterior = geracao_anterior
		geracao_anterior = geracao_n
print(geracao_n)



