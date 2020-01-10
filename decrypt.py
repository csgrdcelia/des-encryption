# -*- coding: utf-8 -*-
from utils.data_manipulation import *
from utils.alpha_binary_conversion import *

def decrypt(message, key):
    # TODO: rounds, etc
    # initial_key_with_empty_check_bits = inverse_permutation(get_encrypted_key_after_first_permutation(), des_constants["CP_1"][0], True)
    # initial_key = remove_check_bits(initial_key_with_empty_check_bits)
    # print(initial_key)
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


def inverse_permutation(encrypted_key, permutation_key, skip_8=False):
    encrypted_key = list(encrypted_key)
    initial_key = [0] * (max(permutation_key) + 1)
    for permutation_index in permutation_key:
        initial_key[permutation_index] = encrypted_key.pop(0)

    if skip_8:
        initial_key = remove_check_bits(initial_key)
    return initial_key


def initial_inverse_permutation(message_part):
    key_pi = des_constants["PI"][0]
    return inverse_permutation(message_part, key_pi)


def inverse_initial_inverse_permutation(message_part):
    key_pi_i = des_constants["PI_I"][0]
    return inverse_permutation(message_part, key_pi_i)


def perform_single_inverse_ronde(left, right, subkey):
    pse = pse_xor_subkey(left, subkey)
    return XOR(pse, right), left


def perform_inverse_ronde(message_part, subkey_array):
    left, right = cut_off(message_part)
    for index in range(15, -1, -1):
        left, right = perform_single_inverse_ronde(left, right, subkey_array[index])

    return left + right


def decrypt_packet(message_part, subkey_array):
    message_part = inverse_initial_inverse_permutation(message_part)
    message_part = perform_inverse_ronde(message_part, subkey_array)
    message_part = initial_inverse_permutation(message_part)

    return message_part


encrypted_message = "iDahEètglJAncFogDRHGxA"

left = "00110000110010100100001000011100"
right = "11010101001001100001000100011010"


def to_int_array(a):
    return [int(i) for i in a]


key = to_int_array("0101111001011011010100100111111101010001000110101011110010010001")
key = permutation(key, des_constants["CP_1"][0], True)
subkey_array = get_subkey_array(key, des_constants["CP_2"][0])

message_part = "0011000011001010010000100001110011010101001001100001000100011010"
# print(cut_off(perform_inverse_ronde(message_part, subkey_array)))


def get_encrypted_key_after_first_permutation():
    key = "11000000000111110100100011110010111101001001011010111111"
    return [int(x) for x in list(key)]
