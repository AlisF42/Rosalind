#!/usr/bin/env python3

import sys
file = sys.argv[1]
rna = []
dna = []
with open(file, 'r') as file:
	for linha in file:
		rnaa = linha.replace("T","U")
		dna = linha.strip()
#		dnaa += linha 
	#	dna.append(linha.strip())
	#	for nuc in linha:
	#		if nuc == "T":
	#			rna.append("U")
	#		else:
	#			rna.append(nuc)
print(dna)
print(rnaa)

