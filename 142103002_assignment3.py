import math


def is_coprime(a, b):
    """Check if two numbers are coprime."""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a == 1


def get_rsa_public_key(phi, N):
    """Calculate the public key 'e' for RSA encryption."""
    for candidate in range(2, phi):
        if is_coprime(phi, candidate) and is_coprime(N, candidate):
            return candidate
    return -1


def get_rsa_private_key(e, phi):
    """Calculate the private key 'd' for RSA decryption."""
    for candidate in range(1, phi):
        if (e * candidate) % phi == 1:
            return candidate
    return -1


def rsa_encrypt(e, N, message):
    """Encrypt a message using RSA."""
    encrypted_message = pow(message, e, N)
    return encrypted_message


def rsa_decrypt(d, N, message):
    """Decrypt a message using RSA."""
    decrypted_message = pow(message, d, N)
    return decrypted_message


def main():
    print("Enter two prime numbers for RSA encryption")
    p = int(input())
    q = int(input())

    print("Enter the number to send")
    message = int(input())

    N = p * q
    phi = (p - 1) * (q - 1)

    # Get public and private keys
    e = get_rsa_public_key(phi, N)
    d = get_rsa_private_key(e, phi)

    print("Public Key (e) is", e)
    print("Private Key (d) is", d)

    ciphertext = rsa_encrypt(e, N, message)
    print("Ciphertext:", ciphertext)

    decrypted_message = rsa_decrypt(d, N, ciphertext)
    print("Decrypted plaintext:", decrypted_message)


if __name__ == "__main__":
    main()
