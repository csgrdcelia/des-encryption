import sys
from encrypt import encrypt


def main():
    action_type = sys.argv[1]
    message = get_file_content(sys.argv[2])
    key = to_int_array(get_file_content(sys.argv[3]))

    if action_type == "encrypt":
        encrypt(message, key)


def get_file_content(file_path):
    file = open(file_path, "r")
    text = file.read()
    file.close()
    return text


def to_int_array(key):
    return [int(i) for i in key]


if __name__ == '__main__':
    main()
