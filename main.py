import random
from sympy import isprime, gcd


MIN_NUMBER = 2
MAX_NUMBER = 10000


def get_random_prime(bits=1024):
    num = MIN_NUMBER * 2
    while not isprime(num):
        num = random.getrandbits(bits)

    return num


def get_coprime(m):
    d = random.randint(2, MAX_NUMBER)
    while gcd(d, m) != 1:
        d = random.randint(2, MAX_NUMBER)

    return d


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1


def keygen():
    p = get_random_prime()
    q = get_random_prime()
    n = p * q
    m = (p - 1) * (q - 1)
    d = get_coprime(m)
    e = modinv(d, m)
    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


public_key, private_key = keygen()


if __name__ == "__main__":
    message = 12345
    ciphertext = encrypt(message, public_key)
    print(f'Encrypted: {ciphertext}')

    decrypted_message = decrypt(ciphertext, private_key)
    print(f'Decrypted: {decrypted_message}')
