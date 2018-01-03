import csv
import os

dossier_de_travail = "//DC1-0210006T/SI - Echange/ISN/MP6 le mastermind"
os.chdir(dossier_de_travail)

nom_csv = "Highscore.csv"

fichier_csv = open(nom_csv, mode='w', newline='')

sortie_csv = csv.writer(fichier_csv, dialect='excel')






