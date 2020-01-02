# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants


def encrypt(file, key):
    des_constants = get_des_constants()
    key = remove_check_bits(key)
    key = first_permutation(key, des_constants["CP_1"][0])


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key


def first_permutation(key, cp1):
    new_key = [0] * 56

    for i in range(0, 62):
        if (i + 1) % 8 == 0:
            continue
        searched_position = i + 1
        index_of_position_in_cp1 = find_index_in_cp1(searched_position, cp1)
        index_in_current_key = i - ((i + 1) / 8)
        new_key[index_of_position_in_cp1] = key[index_in_current_key]
    return new_key


def find_index_in_cp1(searched_position, cp1):
    for i in range(0, 56):
        if cp1[i] == searched_position:
            return i
    raise Exception("Position " + searched_position + " introuvable dans CP1")

