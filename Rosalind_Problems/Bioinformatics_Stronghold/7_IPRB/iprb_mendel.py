#!/usr/bin/env python3

import sys
file = sys.argv[1]


with(open(file, 'r')) as file:
	conteudo = file.read().split()
	k =int(conteudo[0])
	m = int(conteudo[1])
	n = int(conteudo[2])
#k = 2
#m = 2
#n = 2
total = k + m + n


p_kk = k/total * ((k-1)/(total-1))
p_km = k/total * m/(total-1)
p_kn = k/total * n/(total-1)
p_mm = m/total * ((m-1)/(total-1))
p_mn = m/total * n/(total-1)
p_mk = m/total * k/(total -1)
p_nn = n/total * ((n-1)/(total-1))
p_nm = n/total * m/(total -1)
p_nk = n/total * k/(total-1)

p_res = p_mn*(1/2) + p_nm*(1/2) + p_mm*(1/4) + p_nn
p_dom = 1-p_res

print(p_dom)


#k AA  m Aa  n aa

#km   AA AA Aa Aa (4/4)
#kn   Aa Aa Aa Aa (4/4)
#mn  Aa Aa aa aa  (2/4) - 1/2

#kk 4/4 A
#mm 1/4 aa
#nn 4/4 aa













