#!/usr/bin/env python3
import sys

arquivo = sys.argv[1]


with open(arquivo,'r') as arq:
	dados = arq.readline().split()

	a = int(dados[0])
	b = int(dados[1])

soma = 0	
for i in range(a,b+1):
	if i % 2 == 1:
		soma = soma + i
#	else:
#		pass

print(soma)

