import math
import operator
import csv

total_cadeiras = 29
QE = 12684
lista_geral = []
lista_partidos = []
QP = {}
vagasR = {}
eleitos = []
maxV = ''
total_cadeiras_ocupadas = 0
#read csv
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line =(line.split(';'))
        lista_geral.append(list(map(lambda x:x.strip("\n"),line)))
#cria um conjunto de Partidos/coligações
for row in lista_geral:
	name = row[2]
	if len(name.split('-')) == 1:
		lista_partidos.append(name.split('-')[0])
	else:
		lista_partidos.append(name.split('-')[1])

lista_partidos = set(lista_partidos)
lista_partidos = dict.fromkeys(lista_partidos, 0)

#conta os votos para os partidos/coligacoes
for key in lista_partidos.keys():
	for votos in lista_geral:
		if(key in votos[2] and len(votos[2].split('-')) == 1 and key == (votos[2].split('-')[0])):
			lista_partidos[key] = lista_partidos[key]+ int(votos[3])
		elif(key in votos[2] and len(key) >= 6):
			lista_partidos[key] = lista_partidos[key]+ int(votos[3])

#ver QP
for i in lista_partidos:
	if(lista_partidos.get(i) >= QE):
		QP[i] = math.floor(lista_partidos.get(i)/QE)

total_cadeiras_ocupadas = sum(QP.values())

#cadeiras residuais
while total_cadeiras_ocupadas < total_cadeiras:
	for partido in lista_partidos.keys():
		for qp in QP.keys():
			if(partido == qp):
				vagasR[str(partido)] = (lista_partidos.get(partido)/(QP.get(qp)+1))
	maxV = max(vagasR.items(), key=operator.itemgetter(1))[0];
	QP[maxV] += 1
	total_cadeiras_ocupadas+=1

lista_geral = sorted(lista_geral, key = lambda x: (int(x[3])),reverse = True)
#pegar candidatos eleitos por partido
for key in QP.keys():
	i = 0
	for row in lista_geral:
		if(key in row[2] and QP.get(key) > i and len(row[2].split('-')) == 1 and key == (row[2].split('-')[0])):
			eleitos.append(row)
			i = i + 1
		if(key in row[2] and QP.get(key) > i and len(key) >= 6):
			eleitos.append(row)
			i = i + 1
		else:
			pass

#ordena por mais votos
eleitos = sorted(eleitos, key = lambda x: (int(x[3])),reverse = True)

for i,j in enumerate(eleitos):
	eleitos[i] = [" ".join(j)]
#salva no tsv
with open('eleitosFinal.tsv', 'w', newline='') as out_f:
    w = csv.writer(out_f)
    w.writerows(eleitos)