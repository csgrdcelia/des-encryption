# -*- coding: utf-8 -*-
from utils.alpha_binary_conversion import conv_bin
from utils.alpha_binary_conversion import nib_vnoc
from utils.data_manipulation import *


# !LvE.eb!wjKdK,vjOtè -> 100010000011011010100001000100111100101101100000100101001001000000100111011100000101101
#                               00010000000001101000100011100011011000100
def encrypt(message, key):
    key = permutation(key, des_constants["CP_1"][0], True)
    subkey_array = get_subkey_array(key, des_constants["CP_2"][0])

    packets = packet(conv_bin(message))
    encrypt_message = ""
    for pack in packets:
        encrypt_message += list_to_string(encrypt_packet(pack, subkey_array))

    print(nib_vnoc(encrypt_message))


def encrypt_packet(message_part, subkey_array):
    message_part = initial_permutation(message_part)
    left, right = cut_off(message_part)
    left, right = perfom_ronde(left, right, subkey_array)
    message_part = left + right
    return inverse_initial_permutation(message_part)


def initial_permutation(message_part):
    key_pi = des_constants["PI"][0]
    return permutation(message_part, key_pi)


def inverse_initial_permutation(message_part):
    key_pi_i = des_constants["PI_I"][0]
    return permutation(message_part, key_pi_i)


def ronde(left, right, subkey):
    temp_right = pse_xor_subkey(right, subkey)
    temp_right = XOR(temp_right, left)
    return right, temp_right


def perfom_ronde(left, right, subkey_array):
    for index in range(0, 16):
        left, right = ronde(left, right, subkey_array[index])
    return left, right
