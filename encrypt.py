# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    des_constants = get_des_constants()
    key = remove_check_bits(key)
    key = permutation(key, des_constants["CP_1"][0])
    subkey_array = get_subkey_array(key, des_constants["CP_2"][0])


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key


def permutation(key, cp1):
    new_key = [0] * 56

    for i in range(0, 62):
        if (i + 1) % 8 == 0:
            continue
        searched_position = i + 1
        index_of_position_in_cp1 = find_index_in_cp1(searched_position, cp1)
        index_in_current_key = int(i - ((i + 1) / 8))
        new_key[index_of_position_in_cp1] = key[index_in_current_key]
    return new_key


def find_index_in_cp1(searched_position, cp1):
    for i in range(0, len(cp1)):
        if cp1[i] == searched_position:
            return i
    raise Exception("Position " + str(searched_position) + " introuvable dans CP1")


def get_subkey_array(key, cp2):
    debug("clé initiale:", key)
    subkey_array = [[]]
    left_part = key[0:27]
    debug("partie gauche:", left_part)
    right_part = key[28:55]
    debug("partie droite:", right_part)
    for i in range(0,15):
        left_part = shift_bit(left_part)
        debug("partie gauche décalée:", left_part)
        right_part = shift_bit(right_part)
        debug("partie droite décalée:", right_part)
        concat_key = left_part + right_part
        debug("clé concaténée:", concat_key)
        permuted_key = permutation(concat_key, cp2)
        debug("clé permutée:", permuted_key)
        subkey_array.append(permuted_key)
    return subkey_array


def shift_bit(key):
    first_element = key.pop(0)
    key.append(first_element)
    return key


def debug(description, value):
    print(description)
    print(value)
    print()
