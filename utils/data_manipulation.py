from textwrap import wrap


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


def XOR(a, b):
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
