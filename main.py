from commune import Commune

communesFile = open('./input/laposte_hexasmal.csv', encoding='utf8')
adjectiveFile = open('./input/french-word-list-adjectives.csv', 'r')


def readAdjective():
    global adjectiveFile
    adjective = adjectiveFile.readlines()
    adjective = adjective[3::]# supprimer l'entete du fichier
    adjective = [adj for line in adjectives for adj in line.split(';') if adj.isalpha()]

    return adjective


def readCommunes():
    global communesFile
    lines = communesFile.readlines()
    lines = lines[1::]# supprimer l'entete du fichier
    list_commune = []

    for line in lines:
        columns = line.split(';')

        # si les coordonnees gps existe dans le fichier communes
        if columns[5] and columns[5] != '\n':
            gps = columns[5].split(',')
            latitude = gps[0]
            longitude = gps[1]
        else:
            latitude = 0
            longitude = 0

        commune = Commune(columns[0], columns[1], latitude, longitude)
        list_commune.append(commune)

    return list_commune


if __name__ == '__main__':

    adjectives = readAdjective()
    communes = readCommunes()

    print(adjectives)
    print(len(adjectives))

    # for commune in communes:
    #     print(commune)
