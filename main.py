from csv_utils import *
from process import *

if __name__ == '__main__':
    adjectives = readAdjective()
    communes = readCommunes()

    compare_commune_with_Adjective(communes, adjectives)

    print(" total : " + str(len(communes)))
    print(" oil : " + str(number_of_commune_oil(communes)))
    print(" oc : " + str(number_of_commune_oc(communes)))
    print(" neutre : " + str(number_of_commune_neutre(communes)))

    generateOutPut(communes)  # ecrire dans le fichier resultat.csv
