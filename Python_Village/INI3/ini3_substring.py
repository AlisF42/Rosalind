#!/usr/bin/env python3
import sys
arquivo = sys.argv[1]
with open(arquivo,'r') as arquivo:
    linhas = arquivo.readlines() 
    string = linhas[0]
    print(string)
	
    numeros = linhas[1].split()
    a= int(numeros[0])
    b= int(numeros[1])
    c= int(numeros[2])
    d= int(numeros[3])
    subs_1 = string[a:b+1]
    subs_2 = string[c:d+1]
    print(f'{subs_1} {subs_2}')
#with open(arquivo,'r') as arq:
#    linha_num = 0
#    for linha in arq:
#        print(linha)
#        linha_num +=1 
#        if linha_num == 1:
#            s = linha
#        elif linha_num == 2:
#            n = linha.split()
#            f= int(n[0])
#            g= int(n[1])
#            h= int(n[2])
#            i= int(n[3])	
#            sub_1 = s[f:g+1]
#            sub_2 = s[h:i+1] 
#            print(n)
#            print(sub_1, sub_2)
