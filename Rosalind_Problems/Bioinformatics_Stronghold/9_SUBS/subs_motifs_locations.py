#!/usr/bin/env python3

import sys

with open(sys.argv[1],'r') as file:
	conteudo = file.read().split()
	read = conteudo[0]
	motif = conteudo[1]

motif_size = len(motif)
localizacoes = []

for i in range(len(read)-motif_size+1): #pode ser so len(read) mas assi evita itera desne
	if read[i:i+motif_size] == motif:
		loc = i+1
		localizacoes.append(loc)

for i in range(len(localizacoes)):
	print(localizacoes[i],end=" ")
