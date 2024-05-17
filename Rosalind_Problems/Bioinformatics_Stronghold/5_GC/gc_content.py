#!/usr/bin/env python3

import sys

file = sys.argv[1]

def cg_percentage_all(dic):
	percentages_dic = {}
	for i in dic:
		percentages_dic[i] = cg_percentage(dic.get(i))
	return(percentages_dic)


def max_cg2(dic):
	percentages = cg_percentage_all(dic) 	
	key_max = max(percentages, key=percentages.get)
	value_max = percentages[key_max]
	print(key_max)
	print(value_max)

def cg_percentage(seq):
	cg_content = seq.count("C") + seq.count("G")
	cg_decimal = cg_content/len(seq)
	cg_percentage = cg_decimal*100
	return cg_percentage
def max_cg(dic):
	key_max = max(dic, key=dic.get)
	value_max = dic[key_max]
	print(key_max)
	print(value_max)


reads = {}
new_reads ={}
with open(file, 'r') as file:
	for linha in file:
		linha = linha.strip()
		if linha.startswith(">"):
			read_id = linha[1:] #mesma coisa que linha.strip(">").strip()
			reads[read_id] = ''
			seq = ''
		else:	
			reads[read_id] += linha #as vezes é bom deixar separado
			seq += linha #aqui faco tudo junto
			new_reads[read_id] = seq #
			new_reads[read_id] = cg_percentage(seq)#
max_cg2(reads)
max_cg(new_reads)
#print(reads)
#cg_percentage_all(reads)

#chave_maxima = max(reads, key=reads.get)
#print(chave_maxima)
#print(reads[chave_maxima])
#print(reads.get(max(reads.values())))
#print(max(reads.values()))
#print(reads)
#for i in reads:
#	reads[i] = cg_percentage(reads.get(i))
#	print(reads.get(i))
#seq
#seq
#seq = "CCTGCGGAAGGA"	
#cg_content =((seq.count("C") + seq.count("G"))/len(seq))*100
#print(cg_content)
#print(len(seq))
