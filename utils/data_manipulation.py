from textwrap import wrap
from utils.des_constants_extraction import get_des_constants

des_constants = get_des_constants()


def packet(message):
    parts = wrap(message, 64)

    last_part_index = len(parts) - 1
    while len(parts[last_part_index]) < 64:
        parts[last_part_index] += "0"

    return parts


def cut_off(key):
    middle = len(key) // 2
    return key[:middle], key[middle:]


def list_to_string(s):
    index = 0
    while index < len(s):
        s[index] = str(s[index])
        index += 1
    return "".join(s)


def xor(a, b):
    index = 0
    result = ""
    while index < len(a):
        result += str((int(a[index]) + int(b[index])) % 2)
        index += 1
    return result


def left_shift_bit(key):
    first_element = key.pop(0)
    key.append(first_element)
    return key


def cut_6_bit_block(block):
    a = block[0] + block[5]
    b = block[1:5]
    return a, b


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


def expansion(right):
    E = des_constants["E"][0]
    return permutation(right, E)


def xor_with_subkey(subkey_array, right):
    return xor(right, subkey_array)


def convert_block_with_s_key(block, S):
    bin_line, bin_col = cut_6_bit_block(block)
    line_index = int(bin_line, 2)
    col_index = int(bin_col, 2)
    return format(S[line_index][col_index], "04b")


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


def pse_xor_subkey(right, subkey):
    right = expansion(right)
    right = xor_with_subkey(subkey, right)
    right = substitute_block(right)
    return substitute_with_perm(right)


def initial_permutation(message_part):
    key_pi = des_constants["PI"][0]
    return permutation(message_part, key_pi)


def inverse_initial_permutation(message_part):
    key_pi_i = des_constants["PI_I"][0]
    return permutation(message_part, key_pi_i)
