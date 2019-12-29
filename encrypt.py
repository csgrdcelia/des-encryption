from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    des_constants = get_des_constants()
    key = remove_check_bits(key)
    #key = first_permutation(key, des_constants["CP_1"])


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key






