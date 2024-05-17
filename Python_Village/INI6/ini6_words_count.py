#!/usr/bin/env python3

import sys
arquivo = sys.argv[1]
dic = dict()

conteudo = []
with open(arquivo,'r') as arquivo:	
#	conteudo = arquivo.read().split#esse ;e menos eficiente - carrega todo o arquivo de uma vez para dai performar o split
	for i in arquivo:
		palavras = i.split()
		conteudo.extend(palavras)
print(conteudo)
#	for i in arquivo:
#		print(i)
#		a = i.split()
#		print(a) mesma coisa
#print(conteudo) 
with open("teste6.txt", 'w') as new_file:
	for i in conteudo:
		#dic[i] = conteudo.count(i)-> mto mais complexo para cada palavra, rodatoda a lista
		dic[i] = dic.get(i, 0) + 1
#print(dic)
	for chave, valor in dic.items():
		
		#print(chave, valor)
		new_file.write(f"{chave} {valor}\n")
#print(dic.items())

#counts = dict()
#for i in conteudo:
#	counts[i] = counts.get(i, 0) + 1
#print(counts)
