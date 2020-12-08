from csv_utils import *
from process import *

if __name__ == '__main__':
    adjectives = readFile_txt('adjectifs.txt')
    suffix_oil = readFile_txt('suffix_oil.txt')
    suffix_oc = readFile_txt('suffix_oc.txt')

    communes = readCommunes()

    print(suffix_oil)
    print(suffix_oc)

    compare_commune_with_Adjective(communes, adjectives)

    compare_commune_with_suffix(communes, suffix_oil, suffix_oc)

    print(" total : " + str(len(communes)))
    print(" oil : " + str(number_of_commune_oil(communes)))
    print(" oc : " + str(number_of_commune_oc(communes)))
    print(" neutre : " + str(number_of_commune_neutre(communes)))

    generateOutPut(communes)  # ecrire dans le fichier resultat.csv
