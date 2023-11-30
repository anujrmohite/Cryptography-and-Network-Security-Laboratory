import random


def main():
    alphabet = " abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+`{[}]:;'\"<,>.?/|ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ralphabet = alphabet[::-1]

    while True:
        operation = input("Enter Command (e/d/help/exit): ")

        if operation == "e":
            encrypt_message(alphabet, ralphabet)
        elif operation == "d":
            decrypt_message(alphabet, ralphabet)
        elif operation == "exit":
            break
        else:
            print(
                f"Error! Could not find command: {operation}\nPlease run the program again!"
            )


def encrypt_message(alphabet, ralphabet):
    message = input("Enter message to encrypt: ")
    key = get_key_from_message(message)

    if not key:
        key = input("Enter the key (<key>/auto): ")

    if key == "auto":
        key, randstart = generate_key()
    else:
        randstart = extract_start_from_key(key)

    grid, dirInt, reverse = parse_key(key)
    cipher = ""

    for i in range(len(message)):
        plain = message[i]
        index = ralphabet.find(plain) if reverse == "-" else alphabet.find(plain)

        randstart %= 93
        index = (index + randstart) % 93

        cipher += ralphabet[index] if reverse == "-" else alphabet[index]
        randstart += grid + dirInt

    print("Finished!")
    print(
        "\nPlaintext:\n"
        + message
        + "\n\nCiphertext:\n"
        + cipher
        + "\n\nKey:\n"
        + key
        + "\n\nExport (Ciphertext is before ~, Key is after ~):\n"
        + cipher
        + "~"
        + key
    )


def decrypt_message(alphabet, ralphabet):
    message = input("Enter Ciphertext or Export text to decrypt: ")
    key = get_key_from_message(message)

    if not key:
        key = input("Enter the key (<key>/auto): ")

    grid, dirInt, reverse = parse_key(key)
    randstart = extract_start_from_key(key)
    cipher = ""

    for i in range(len(message)):
        plain = message[i]
        index = alphabet.find(plain) if reverse == "-" else ralphabet.find(plain)

        randstart %= 93
        index = (index + randstart) % 93

        cipher += alphabet[index] if reverse == "-" else ralphabet[index]
        randstart += grid + dirInt

    print("Finished!")
    print(
        "\nCiphertext:\n" + message + "\n\nPlaintext:\n" + cipher + "\n\nKey:\n" + key
    )


def get_key_from_message(message):
    if "~" in message:
        kIndex = message.find("~")
        key = message[kIndex + 1 :]
        return key
    return ""


def generate_key():
    grid = random.randint(10, 99)
    grid_sqr = grid**2 - 1
    randstart = random.randint(0, grid_sqr)
    reverse = random.choice(["-", "+"])
    dir_int = random.randint(10, grid) % 100

    if dir_int == 0:
        dir_int = 10

    key = f"{grid}({reverse}{dir_int}){randstart}"
    return key, randstart


def extract_start_from_key(key):
    parts = key.split("(")
    randstart = int(parts[1].split(")")[1])
    return randstart


def parse_key(key):
    grid = int(key[:2])
    reverse = key[3]
    dir_int = int(key[4:6])
    return grid, dir_int, reverse


if __name__ == "__main__":
    main()
