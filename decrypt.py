# -*- coding: utf-8 -*-
from utils.des_constants_extraction import get_des_constants
from textwrap import wrap

def decrypt(message, key):
    # TODO: rounds, etc
    initial_key_with_empty_check_bits = inverse_permutation(get_encrypted_key_after_first_permutation(), des_constants["CP_1"][0], True)
    initial_key = remove_check_bits(initial_key_with_empty_check_bits)
    print(initial_key)


def delete_8th_multiple_index(key):
    result = []
    bits = len(key)
    for index in range(0, bits):
        element = str(key.pop(0))
        if (index + 1) % 8 != 0:
            result.append(element)
        index += 1
    return result


def inverse_permutation(encrypted_key, permutation_key, skip_8=False):
    initial_key = [0] * (max(permutation_key) + 1)
    for permutation_index in permutation_key:
        initial_key[permutation_index] = encrypted_key.pop(0)

    if skip_8:
        initial_key = delete_8th_multiple_index(initial_key)
    return initial_key


def list_to_string(s):
    index = 0
    while index < len(s):
        s[index] = str(s[index])
        index += 1
    return "".join(s)


def test_inverse_permutation(permutation_key_name, permuted_binary_string, expected_binary_string, skip_8=False):
    entry = wrap(permuted_binary_string, 1)
    permutation_key = des_constants[permutation_key_name][0]

    print(permutation_key_name + " : " +
          str(list_to_string(inverse_permutation(entry, permutation_key, skip_8)) == expected_binary_string))


des_constants = get_des_constants()

test_inverse_permutation(permutation_key_name="CP_1",
                         permuted_binary_string="11000000000111110100100011110010111101001001011010111111",
                         expected_binary_string="01011110101101010100101111110101000000110110111101001000",
                         skip_8=True)

test_inverse_permutation(permutation_key_name="PI",
                         permuted_binary_string="0111110110101011001111010010101001111111101100100000001111110010",
                         expected_binary_string="1101110010111011110001001101010111100110111101111100001000110010")

test_inverse_permutation(permutation_key_name="E",
                         permuted_binary_string="001111111111110110100100000000000111111110100100",
                         expected_binary_string="01111111101100100000001111110010")

test_inverse_permutation(permutation_key_name="PERM",
                         permuted_binary_string="10100011010001111110110111100110",
                         expected_binary_string="01010001111010111111000100110111")

test_inverse_permutation(permutation_key_name="PI_I",
                         permuted_binary_string="1000100000110110101000010001001111001011011000001001010010010000",
                         expected_binary_string="0011000011001010010000100001110011010101001001100001000100011010")

def remove_check_bits(key):
    new_key = []
    for index, number in enumerate(key, start=1):
        if index % 8 != 0:
            new_key.append(number)
    return new_key

def get_encrypted_key_after_first_permutation():
    key = "11000000000111110100100011110010111101001001011010111111"
    return [int(x) for x in list(key)]
