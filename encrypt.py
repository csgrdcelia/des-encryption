

def encrypt(file, key):
    key = remove_check_bits(key)


def remove_check_bits(key):
    new_key = ""
    for index, char in enumerate(key, start=1):
        if index % 8 != 0:
            new_key += char
    return new_key
