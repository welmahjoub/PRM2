import csv

from classe import Commune


# lire le fichier des adjectif francais
def readAdjective(adjectiveFile):
    adjective = adjectiveFile.readlines()
    adjective = adjective[3::]  # supprimer l'entete du fichier
    adjective = [adj for line in adjective for adj in line.split(';') if adj.isalpha()]

    return adjective


# lire le fichier insee commune
def readCommunes(communesFile):
    lines = communesFile.readlines()
    lines = lines[1::]  # supprimer l'entete du fichier
    list_commune = dict()

    for line in lines:

        columns = line.split(';')

        # si les coordonnees gps existe dans le fichier communes
        if columns[5] and columns[5] != '\n':
            gps = columns[5].split(',')
            latitude = float(gps[0])
            longitude = float(gps[1])
        else:
            latitude = 0.0
            longitude = 0.0

        code = columns[0]
        name = columns[1]
        code_postal=columns[2]
        commune = Commune(code, name, code_postal, latitude, longitude)
        list_commune[code] = commune # ajouter la commune dans la liste

    return list_commune

# ecrire la liste des communes dans le fichier result.csv 
def generateOutPut(communes):
    with open('output/result.csv', 'w', newline='') as file:
        fieldnames = ['code', 'name', 'code_postal', 'latitude', 'longitude', 'score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for commune in communes.values():
            writer.writerow({'code': commune.code, 'name': commune.name, 'code_postal': commune.code_postal
                                , 'latitude': commune.latitude, 'longitude': commune.longitude, 'score': commune.score})