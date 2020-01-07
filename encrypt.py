# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants
from textwrap import wrap


def encrypt(file, key):
    key = permutation(key, des_constants["CP_1"][0], True)
    subkey_array = get_subkey_array(key, des_constants["CP_2"][0])


def permutation(initial_key, permutation_key, skip_8=False):
    new_key = []
    for permutation_index in permutation_key:
        if skip_8:
            if (permutation_index + 1) % 8 == 0:
                continue
        new_key.append(initial_key[permutation_index])
    return new_key


def get_subkey_array(key, cp2):
    subkey_array = []
    left_part, right_part = cut_off(key)
    for i in range(0, 15):
        concat_key = shift_bit(left_part) + shift_bit(right_part)
        permuted_key = permutation(concat_key, cp2)
        subkey_array.append(permuted_key)
        print(permuted_key)
    return subkey_array


def shift_bit(key):
    first_element = key.pop(0)
    key.append(first_element)
    return key


def packet(message):
    parts = wrap(message, 64)

    last_part_index = len(parts) - 1
    while len(parts[last_part_index]) < 64:
        parts[last_part_index] += "0"

    return parts


def initial_permutation(message_parts):
    index = 0
    key_pi = des_constants["PI"][0]

    while index < len(message_parts):
        message_parts[index] = permutation(message_parts[index], key_pi)
        index += 1

    return message_parts


def cut_off(key):
    middle = len(key) // 2
    return key[:middle], key[middle:]


des_constants = get_des_constants()
