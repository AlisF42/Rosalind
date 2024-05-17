#!/usr/bin/env python3

import sys

with open(sys.argv[1],'r') as file:
	conteudo = file.read().split()
	k = int(conteudo[0])
	m = int(conteudo[1])
	n = int(conteudo[2])

total = k+m+n
twoRes = (n/total)* ((n-1)/(total-1))
twoHetero = (m/total) * ((m-1)/(total-1))
Aaaa = (m/total)*(n/(total-1))
aaAa = (n/total)*(m/(total-1))
heteroRes = Aaaa + aaAa

p_res = twoRes + (twoHetero*1/4) + (Aaaa*1/2) + (aaAa*1/2)
p_dom = 1- p_res
print(p_dom)
print("="*58)
p_res2 = twoRes + (twoHetero*1/4) + (heteroRes*1/2) 
p_dom2 = 1- p_res2
print(p_dom2)

#k = 100%  dominante AA 
#m = 75% dominante Aa
#n = 0% dominante aa

#quando pode vir recessivo
#aa e aa n/total * n-1/total-1
#Aa e Aa (m/total * m-1/total-1)
#Aa e aa (m/total * n/total-1)
#aa e Aa (n/total * m/total-1)

#p de ser recessivo 
#2ress + 2hetero*1/4 + heteroRes*1/2 + heteroRes*1/2
#

#total = k + m + n
#p_dois_dominate
#p_primeiro_k = (k/total) 
#p_primeiro_m = m/total
#p_primeiro_n = n/total

#p_segundo_k = 

