# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    key = permutation(key, des_constants["CP_1"][0])


def permutation(initial_key, permutation_key):
    new_key = []

    for permutation_index in permutation_key:
        if (permutation_index + 1) % 8 == 0:
            continue

        new_key.append(initial_key[permutation_index])
    return new_key


des_constants = get_des_constants()
