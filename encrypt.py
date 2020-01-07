# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    key = permutation(key, des_constants["CP_1"][0])
    #subkey_array = get_subkey_array(key, des_constants["CP_2"][0])


def permutation(initial_key, permutation_key):
    new_key = []
    for permutation_index in permutation_key:
        if (permutation_index + 1) % 8 == 0:
            continue
        new_key.append(initial_key[permutation_index])
    return new_key


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

des_constants = get_des_constants()
