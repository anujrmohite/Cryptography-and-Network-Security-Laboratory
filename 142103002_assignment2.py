class VigenereCipher:
    def __init__(self, keyword):
        """Initialize VigenereCipher object with a keyword."""
        self.keyword = keyword.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _shift_letter(self, letter, shift, encrypt=True):
        """Shift a letter by a specified amount."""
        if letter.upper() in self.alphabet:
            index = self.alphabet.index(letter.upper())
            shift = shift if encrypt else -shift
            return self.alphabet[(index + shift) % 26]
        else:
            return letter

    def _apply_cipher(self, text, encrypt=True):
        """Apply the Vigenere cipher to the given text."""
        result = ""
        keyword_length = len(self.keyword)
        for i, char in enumerate(text):
            shift = self.alphabet.index(self.keyword[i % keyword_length])
            result += self._shift_letter(char, shift, encrypt)
        return result

    def encrypt(self, plaintext):
        """Encrypt the plaintext using the Vigenere cipher."""
        return self._apply_cipher(plaintext, encrypt=True)

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext using the Vigenere cipher."""
        return self._apply_cipher(ciphertext, encrypt=False)


# Example usage
keyword = "KEYWORD"
plaintext = "HELLO WORLD"

# Create a VigenereCipher object
cipher = VigenereCipher(keyword)

# Encrypt and decrypt the plaintext
ciphertext = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(ciphertext)

# Display the results
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")
