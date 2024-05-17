#!/usr/bin/env python3

import sys

arquivo = sys.argv[1]
contador = 0

with open("testebrabo.txt",'w') as novo_arquivo:
	with open(arquivo, 'r') as arquivo:
		for i in arquivo:
			contador += 1
			if contador % 2 != 1:
				novo_arquivo.write(i)
			else:
				pass

print("Concluido!") 		
