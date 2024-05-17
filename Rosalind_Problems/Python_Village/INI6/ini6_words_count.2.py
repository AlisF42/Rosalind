#!/usr/bin/env python3

import sys
arquivo = sys.argv[1]

with open(arquivo,'r') as arquivo:
	for linha in arquivo:
		linha = linha.replace('.','').replace('.','').lower()
		palavras = linha.split()
contagem = {}
for palavra in palavras:
	if palavra in contagem:
		contagem[palavra] += 1
	else:
		contagem[palavra] = 1

for key, value in contagem.items():
	print(f'{key}: {value}')



print('========')
print(contagem)
print('=======')
print(contagem.items())
print(list(contagem.items()))

