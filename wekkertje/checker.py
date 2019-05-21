from functools import reduce


def check(verbose=False):

    # %%

    with open("geheimwoordje.txt", mode="r") as f:
        geheimwoordje_text = f.readline()
    with open("sleutel.txt", mode="r") as f:
        sleutel_text = f.readline()
    with open("antwoord.txt", mode="r") as f:
        antwoord_text = f.readline()

    # %%

    # geheimwoordje.txt bevat:
    # een of meerdere woorden; leestekens en spaties worden genegeerd, alle letters worden hoofdletters
    toegestaan = "abcdefghijklmnopqrstuvwxyz"
    geheimwoordje_verwerkt = "".join(char for char in geheimwoordje_text.lower() if char in toegestaan)
    if verbose:
        print("Verwerkt: {}".format(geheimwoordje_verwerkt))

    # toets  0   1   2      3      4      5      6      7       8      9
    nokia = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    welke_toets = lambda char: next(toets for toets, letters in enumerate(nokia) if char in letters)

    geheimwoordje_gecodeerd = list(map(welke_toets, geheimwoordje_verwerkt))

    geheime_code = reduce(lambda x, y: 10 * x + y, geheimwoordje_gecodeerd)
    if verbose:
        print("Geheime code: {}".format(geheime_code))

    # Bijvoorbeeld:
    # -------
    # geheimwoordje_text == "app EL!"
    #  ->
    # geheimwoordje_verwerkt == "appel"
    #  ->
    # geheimwoordje_gecodeerd == [2, 7, 7, 3, 5]
    #  ->
    # geheime_code == 27735

    # %%

    # sleutel.txt bevat:
    # twee ints, gescheiden door een komma of spatie
    sleutel = [int(s) for s in sleutel_text.replace(",", " ").split(" ")]
    assert(len(sleutel) == 2)

    antwoord_moet_zijn = (geheime_code * sleutel[0]) % sleutel[1]
    if verbose:
        print("Antwoord moet zijn: {}".format(antwoord_moet_zijn))

    # %%

    # antwoord.txt bevat:
    # een int

    antwoord_gegeven = int(antwoord_text)
    if verbose:
        print("Antwoord gegeven: {}".format(antwoord_gegeven))

    return antwoord_gegeven == antwoord_moet_zijn


if __name__ == "__main__":
    assert(check(True))
