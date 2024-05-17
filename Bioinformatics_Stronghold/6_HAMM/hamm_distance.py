#!/usr/bin/env python3

import sys
file = sys.argv[1]

with open(file, 'r') as file:
	conteudo = file.readlines()

a = conteudo[0].strip()
b= conteudo[1].strip()
count = 0
i = 0
while i < len(a):
	if a[i] != b[i]:
		count += 1
		i += 1
	else:
		i+=1
print(count)

hamming = 0
for i in range(len(a)):
	if a[i] != b[i]:
		hamming +=1 
print(hamming)
d = 0
for x1, x2 in zip(a,b):
	if x1 != x2:
		d += 1
print(d)


