# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants

def decrypt(message, key):
    # TODO: rounds, etc
    initial_key_with_empty_check_bits = inverse_permutation(get_encrypted_key_after_first_permutation(), des_constants["CP_1"][0], True)
    initial_key = remove_check_bits(initial_key_with_empty_check_bits)
    print(initial_key)


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key


def inverse_permutation(encrypted_key, permutation_key, skip_8=False):
    initial_key = [0] * (max(permutation_key) + 1)
    for permutation_index in permutation_key:
        initial_key[permutation_index] = encrypted_key.pop(0)

    if skip_8:
        initial_key = remove_check_bits(initial_key)
    return initial_key


def list_to_string(s):
    index = 0
    while index < len(s):
        s[index] = str(s[index])
        index += 1
    return "".join(s)


des_constants = get_des_constants()


def get_encrypted_key_after_first_permutation():
    key = "11000000000111110100100011110010111101001001011010111111"
    return [int(x) for x in list(key)]
