# -*- coding: utf-8 -*-
from utils.alpha_binary_conversion import conv_bin
from utils.alpha_binary_conversion import nib_vnoc
from utils.des_constants_extraction import get_des_constants
from utils.data_manipulation import *
from textwrap import wrap

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
    for i in range(0, 16):
        concat_key = left_shift_bit(left_part) + left_shift_bit(right_part)
        permuted_key = permutation(concat_key, cp2)
        subkey_array.append(permuted_key)
    return subkey_array


def initial_permutation(message_part):
    key_pi = des_constants["PI"][0]
    return permutation(message_part, key_pi)


def inverse_initial_permutation(message_part):
    key_pi_i = des_constants["PI_I"][0]
    return permutation(message_part, key_pi_i)


def convert_block_with_s_key(block, S):
    bin_line, bin_col = cut_6_bit_block(block)
    line_index = int(bin_line, 2)
    col_index = int(bin_col, 2)
    return format(S[line_index][col_index], "04b")


def expansion(right):
    E = des_constants["E"][0]
    return permutation(right, E)


def XOR_with_subkey(subkey_array, right):
    return XOR(right, list_to_string(subkey_array))


def substitute_block(calculated_right):
    result = ""
    right_parts = wrap(calculated_right, 6)
    S = des_constants["S"]
    for index in range(0, 8):
        result += convert_block_with_s_key(right_parts[index], S[index])
    return result


def substitute_with_perm(calculated_right):
    perm = des_constants["PERM"][0]
    return permutation(calculated_right, perm)


def ronde(left, right, subkey_array):
    calculated_right = expansion(right)
    calculated_right = XOR_with_subkey(subkey_array, calculated_right)
    calculated_right = substitute_block(calculated_right)
    calculated_right = list_to_string(substitute_with_perm(calculated_right))
    calculated_right = XOR(calculated_right, left)
    return right, calculated_right


def perfom_ronde(left, right, subkey_array):
    for index in range(0, 16):
        left, right = ronde(left, right, subkey_array[index])
    return left, right


des_constants = get_des_constants()
