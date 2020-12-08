def compare_commune_with_Adjective(communes, adjective):
    for commune in communes.values():

        if commune.name.startswith(tuple(adjective)):  # oil :adjectif precede le nom
            commune.score = -1

        if commune.name.endswith(tuple(adjective)):  # oc : adjectif suit le nom
            commune.score = 1


def compare_commune_with_suffix(communes, suffix_oil, suffix_oc):
    for commune in communes.values():

        if commune.name.endswith(tuple(suffix_oil)):  # oil :adjectif precede le nom
            commune.score = -1

        if commune.name.endswith(tuple(suffix_oc)):  # oc : adjectif suit le nom
            commune.score = 1

def number_of_commune_oil(communes):
    return sum(1 for commune in communes.values() if commune.score == -1)


def number_of_commune_oc(communes):
    return sum(1 for commune in communes.values() if commune.score == 1)


def number_of_commune_neutre(communes):
    return sum(1 for commune in communes.values() if commune.score == 0)
