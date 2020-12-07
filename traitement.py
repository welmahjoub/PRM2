

def compare_commune_with_Adjective(communes, adjective):

    for commune in communes.values():

        if commune.name.startswith(tuple(adjective)):
            commune.score = -1

        if commune.name.endswith(tuple(adjective)):
            commune.score = 1



def number_of_commune_oil(communes):
    return sum(1 for commune in communes.values() if commune.score == -1)


def number_of_commune_oc(communes):
    return sum(1 for commune in communes.values() if commune.score == 1)


def number_of_commune_neutre(communes):
    return sum(1 for commune in communes.values() if commune.score == 0)
