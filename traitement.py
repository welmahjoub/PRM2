


def compareAdjective(communes, adjective):
    for code, commune in communes.items():

        for adj in adjective:
            if commune.name.startswith(adj):
                commune.score = -1

            if commune.name.endswith(adj):
                commune.score = 1


def number_of_commune_oil(communes):
    return sum(1 for commune in communes.values() if commune.score == -1)


def number_of_commune_oc(communes):
    return sum(1 for commune in communes.values() if commune.score == 1)


def number_of_commune_neutre(communes):
    return sum(1 for commune in communes.values() if commune.score == 0)
