from os import system,listdir
from random import choice
from string import ascii_letters,digits
from time import sleep

# sera usado para gerar strings aleatorias
CHARS = ascii_letters+digits

if __name__=="__main__":
	# criacao e copia dos arquivos do diretorio atual
	system("mkdir renomeados")
	originais = listdir()
	originais.remove("rnCB.py")
	originais.remove("renomeados")

	# detecta arquivos de formatacao invalida
	invalidos = []
	for x in originais:
		if len(x)<6 or (len(x)>6 and x[6] != "."):
			print(f"arquivo {x} nao corresponde a formatacao catbox")
			invalidos.append(x)

	# remove invalidos da lista de arquvos que serao alterados
	for x in invalidos:
		originais.remove(x)

	for x in originais:
		system(f"cp {x} renomeados")

	# renomeia arquivos copiados com string aleatoria de 20 caracteres
	for x in originais:
		nome=""
		for y in range(20):
			nome += choice(CHARS)
		extensao = x[6:]
		novo_nome = nome + extensao
		system(f"mv renomeados/{x} renomeados/{novo_nome}")