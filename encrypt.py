# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    key = permutation(key, des_constants["CP_1"][0], True)
    subkey_array = get_subkey_array(key, des_constants["CP_2"][0])


def permutation(initial_key, permutation_key, skip_8):
    new_key = []
    for permutation_index in permutation_key:
        if skip_8:
            if (permutation_index + 1) % 8 == 0:
                continue
        new_key.append(initial_key[permutation_index])
    return new_key


def get_subkey_array(key, cp2):
    subkey_array = []
    left_part, right_part = key[0:28], key[28:56]
    for i in range(0, 15):
        concat_key = shift_bit(left_part) + shift_bit(right_part)
        permuted_key = permutation(concat_key, cp2, False)
        subkey_array.append(permuted_key)
    return subkey_array


def shift_bit(key):
    first_element = key.pop(0)
    key.append(first_element)
    return key


des_constants = get_des_constants()
