#coding utf-8

import csv

fichier = "grants.csv"

f1 = open(fichier)

lignes = csv.reader(f1)

n = 0

# for ligne in lignes:
# 	n +=1
# 	if ligne[4] == "Aide aux éditeurs":

# 	elif ligne [4] == "Innovation commerciale":

# 	elif ligne [4] == "Initiatives collectives"
# 		print(ligne)

for ligne in lignes:
	n +=1
	if ligne[3] == "Fonds du Canada pour les périodiques":
		print(ligne)

	else:

		liste = [0]
		print (liste)


