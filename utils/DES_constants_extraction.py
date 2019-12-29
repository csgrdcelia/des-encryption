# Récupère un tableau associatif avec les constantes du chiffrement DES
def get_des_constants():
    file = open("DES_constants.txt", "r")
    txt = file.read()
    file.close()

    line_break = '\n'

    constant_dictionary = dict()

    # Permutation initiale
    key = "PI"
    constant_dictionary[key] = zero_matrix(1, 64)
    start = txt.find(key + ' =')
    end = txt.find('FIN ' + key)
    column = 0
    while txt[start] != line_break and start < end:
        start += 1
    start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 64
        while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end: start += 1

        column += 1

        # Permutation initiale inverse
        key = "PI_I"
        constant_dictionary[key] = zero_matrix(1, 64)
        start = txt.find(key + ' =')
        end = txt.find('FIN ' + key)
        column = 0
        while txt[start] != line_break and start < end:
            start += 1
        start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 64
        while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end: start += 1

        column += 1

    # Fonction d'expantion
    key = "E"
    constant_dictionary[key] = zero_matrix(1, 48)
    start = txt.find(key + ' =')
    end = txt.find('FIN ' + key)
    column = 0
    while txt[start] != line_break and start < end: start += 1
    start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 48
        while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end: start += 1

        column += 1

    # Permutation
    key = "PERM"
    constant_dictionary[key] = zero_matrix(1, 32)
    start = txt.find(key + ' =')
    end = txt.find('FIN ' + key)
    column = 0
    while txt[start] != line_break and start < end: start += 1
    start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while (ord('0') <= ord(txt[start]) <= ord('9') and start < end):
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 32
        while (not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end): start += 1

        column += 1

    # Première permutation des clefs
    key = "CP_1"
    constant_dictionary[key] = zero_matrix(1, 56)
    start = txt.find(key + ' =')
    end = txt.find('FIN ' + key)
    column = 0
    while txt[start] != line_break and start < end: start += 1
    start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 56
        while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end: start += 1

        column += 1

    # Seconde permutation des clefs
    key = "CP_2"
    constant_dictionary[key] = zero_matrix(1, 48)
    start = txt.find(key + ' =')
    end = txt.find('FIN ' + key)
    column = 0
    while txt[start] != line_break and start < end: start += 1
    start += 1
    while start < end:
        constant_dictionary[key][0][column] = 0
        while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
            constant_dictionary[key][0][column] = 10 * constant_dictionary[key][0][column] + int(txt[start])
            start += 1
        constant_dictionary[key][0][column] -= 1  # Car les entiers sont entre 1 et 48
        while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end: start += 1

        column += 1

    # Les 8 fonctions de substitution (numéroté de 0 à 7)
    key = "S"
    constant_dictionary[key] = dict()
    for i in range(0, 8):
        constant_dictionary[key][i] = zero_matrix(4, 16)
        start = txt.find(key + str(i + 1) + ' =')
        end = txt.find('FIN ' + key + str(i + 1))
        column = 0
        line = 0
        while txt[start] != line_break and start < end: start += 1
        start += 1
        while start < end:
            constant_dictionary[key][i][line][column] = 0
            while ord('0') <= ord(txt[start]) <= ord('9') and start < end:
                constant_dictionary[key][i][line][column] = 10 * constant_dictionary[key][i][line][column] + int(txt[start])
                start += 1

            while not (ord('0') <= ord(txt[start]) <= ord('9')) and start < end:
                if txt[start] == line_break and column >= 0:
                    line += 1
                    column = -1
                start += 1

            column += 1

    return constant_dictionary


def zero_matrix(x, y):
    return [[0] * y for _ in range(x)]