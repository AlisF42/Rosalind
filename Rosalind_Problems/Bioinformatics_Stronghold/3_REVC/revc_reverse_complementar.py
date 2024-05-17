#!/usr/bin/env python3

import sys
file = sys.argv[1]
trans = str.maketrans('ATGC', 'TACG')
with open(file,'r') as file:
	for linha in file:
		dna = linha.strip()
		reverso = linha[::-1]
		reverso2 = linha[::-1].translate(trans)
a = "I wonder how this text looks like backwards"
print(dna)
print(reverso2)
print(a[::-1])
