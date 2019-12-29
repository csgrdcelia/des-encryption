import sys
from encrypt import encrypt


def main():
    action_type = sys.argv[1]
    file = get_file_content(sys.argv[2])
    key = get_file_content(sys.argv[3])

    if action_type == "encrypt":
        encrypt(file, key)


def get_file_content(file_path):
    file = open(file_path, "r")
    text = file.read()
    file.close()
    return text


if __name__ == '__main__':
    main()
