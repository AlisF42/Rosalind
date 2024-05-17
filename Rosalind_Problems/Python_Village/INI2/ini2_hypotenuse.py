#!/usr/bin/env python3
#print("Calculando o quadrado da hipotenusa")
#a = int(input("De um numero: "))
#b = int(input("De um outro numero: "))
#c = a**2 + b**2
#print(c)

#arquivo = input("escreva o nome do arquivo: ")
#arq = open(arquivo, 'r')
#conteudo = arq.read()
#a = int(conteudo.split(' ')[0])
#b = int(conteudo.split(' ')[1])
#print(a,b)
import sys

if len(sys.argv) != 2:
	print("Uso: python script.py <nome_do_arquivo>")
	sys.exit(1)

arquivo = sys.argv[1]

try:
    with open(arquivo, 'r') as arquivo:
        numeros = arquivo.readline().strip().split()
        a = int(numeros[0])
        b = int(numeros[1])
        h = a**2 + b**2
        print("Hipotenusa ao quadrado = ", h)
except FileNotFoundError:
    print("Arquivo não encontrado:", arquivo)
except ValueError:
    print("Conteúdo do arquivo não está no formato esperado.")




