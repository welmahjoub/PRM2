from csv_utils import *
from traitement import *

communesFile = open('./input/laposte_hexasmal.csv', encoding='utf8')
adjectiveFile = open('./input/french-word-list-adjectives.csv', 'r')


if __name__ == '__main__':

    adjectives = readAdjective(adjectiveFile)
    communes = readCommunes(communesFile)

    compare_commune_with_Adjective(communes, adjectives)

    print(" total : "+str(len(communes)))
    print(" oil : " + str(number_of_commune_oil(communes)))
    print(" oc : " + str(number_of_commune_oc(communes)))
    print(" neutre : " + str(number_of_commune_neutre(communes)))

    generateOutPut(communes)# ecrire dans le fichier resultat.csv