import random


class DiffieHellman:
    def __init__(self, prime=None, base=2, bits=512):
        # Use a fixed large prime number if not provided
        self.prime = (
            prime
            if prime
            else 0x00C037C37588B4329887E61C2DA3324B1BA4B81A63F9748FEA5B9D656E34A793
        )
        self.base = base  # commonly used base
        self.private_key = random.getrandbits(bits)
        self.public_key = self._mod_pow(self.base, self.private_key, self.prime)

    @staticmethod
    def _mod_pow(base, exponent, modulus):
        """Efficient exponentiation (base^exponent % modulus)."""
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent >> 1
            base = (base * base) % modulus
        return result

    def generate_shared_secret(self, other_public_key):
        """Generate the shared secret using the other party's public key."""
        return self._mod_pow(other_public_key, self.private_key, self.prime)


# Example usage
alice = DiffieHellman()
bob = DiffieHellman()

alice_shared_secret = alice.generate_shared_secret(bob.public_key)
bob_shared_secret = bob.generate_shared_secret(alice.public_key)

assert alice_shared_secret == bob_shared_secret
print(f"The shared secret is: {alice_shared_secret}")
