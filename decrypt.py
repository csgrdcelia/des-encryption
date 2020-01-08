# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def decrypt(message, key):
    # TODO: rounds, etc
    initial_key_with_empty_check_bits = inverse_permutation(get_encrypted_key_after_first_permutation(), des_constants["CP_1"][0], True)
    initial_key = remove_check_bits(initial_key_with_empty_check_bits)
    print(initial_key)


def inverse_permutation(encrypted_key, permutation_key, skip_8):
    list_length = len(permutation_key) + 8
    initial_key = [0] * list_length
    for permutation_index in permutation_key:
        if skip_8:
            if (permutation_index + 1) % 8 == 0:
                continue
        initial_key[permutation_index] = encrypted_key.pop(0)
    return initial_key


des_constants = get_des_constants()


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key

def get_encrypted_key_after_first_permutation():
    key = "11000000000111110100100011110010111101001001011010111111"
    return [int(x) for x in list(key)]

