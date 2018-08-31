import math
import operator


total_cadeiras = 29
QE = 12684
listaC = []
listaP = []
QP = {}
total_cadeiras_ocupadas = 0
#read csv
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line =(line.split(';'))
        listaC.append(list(map(lambda x:x.strip(),line)))
#create a set of Partidos/coligações
for row in listaC:
	listaP.append(row[2])

listaP = set(listaP)
listaP = dict.fromkeys(listaP, 0)
#conta os votos para os partidos/coligacoes
for key in listaP.keys():
	for votos in listaC:
		if(votos[2] == key):
			listaP[key] += int(votos[3]) 
#ver QP
for i,value in enumerate(listaP.values()):
	temp = list(listaP.keys())
	QP[temp[i]] = math.floor(value/QE)

total_cadeiras_ocupadas = sum(QP.values())

print(QP)
print("total_cadeiras_ocupadas: " + str(total_cadeiras_ocupadas))