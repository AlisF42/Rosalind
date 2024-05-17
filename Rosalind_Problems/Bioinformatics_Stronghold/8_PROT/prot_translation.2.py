#!/usr/bin/env python3

import sys


#Importando e criando dicionario
def codon_table(file):
	with open(file,'r') as file:
		conteudo = file.read().split()
		codon_table = {}
	for i in range(0, len(conteudo),2):
		key = conteudo[i]
		value = conteudo[i+1]
		codon_table[key] = value
	return codon_table


with open(sys.argv[1],'r') as file:
	mrna = file.read().strip()
protein = ''
codon_table = codon_table(sys.argv[2])
for i in range(0,len(mrna),3):
	codon = mrna[i:i+3]
	aminoacid = codon_table.get(codon, "Stop")
	if aminoacid == "Stop":
		break
	else:
		protein += aminoacid

print(protein)


