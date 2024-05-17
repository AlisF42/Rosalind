#!/usr/bin/env python3

import sys
file = sys.argv[1]
sequence =[]
contagem_nuc = {}
with open(file,'r') as file:
	for linha in file:
		linha = linha.strip()
#		A += linha.count("A")
#		C = linha.count("C")
		for letra in linha:
			contagem_nuc[letra] = contagem_nuc.get(letra,0)+1
			
print(f'{contagem_nuc["A"]} {contagem_nuc["C"]} {contagem_nuc["G"]} {contagem_nuc["T"]}')	
for x, y in contagem_nuc.items():
	print(f"{y}",end=' ') 
#print(f"A:{A} C: {C}")
