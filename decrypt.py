# -*- coding: utf-8 -*-
from utils.data_manipulation import *
from utils.alpha_binary_conversion import conv_bin
from utils.alpha_binary_conversion import nib_vnoc


def decrypt(message, key):
    key = permutation(key, des_constants["CP_1"][0], True)
    subkey_array = get_subkey_array(key, des_constants["CP_2"][0])

    packets = packet(conv_bin(message))
    encrypt_message = ""
    for pack in packets:
        encrypt_message += list_to_string(decrypt_packet(pack, subkey_array))

    print(nib_vnoc(encrypt_message))


def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key


def perform_single_inverse_ronde(left, right, subkey):
    pse = pse_xor_subkey(left, subkey)
    return xor(pse, right), left


def perform_inverse_ronde(message_part, subkey_array):
    left, right = cut_off(message_part)
    for index in range(15, -1, -1):
        left, right = perform_single_inverse_ronde(left, right, subkey_array[index])

    return left + right


def decrypt_packet(message_part, subkey_array):
    message_part = initial_permutation(message_part)
    message_part = perform_inverse_ronde(message_part, subkey_array)
    message_part = inverse_initial_permutation(message_part)

    return message_part
