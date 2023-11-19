import random


def is_prime(n, k=5):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, n - 1, n)
        if x != 1:
            return False
    return True


def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi - 1)
    while extended_gcd(e, phi)[0] != 1:
        e = random.randint(1, phi - 1)

    d = modinv(e, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg


def decrypt(encrypted_msg, private_key):
    d, n = private_key
    decrypted_msg = [chr(pow(char, d, n)) for char in encrypted_msg]
    return ''.join(decrypted_msg)


bits = 512
public_key, private_key = generate_keypair(bits)

print(f"Відкритий ключ (e, n): {public_key}")
print(f"Закритий ключ (d, n): {private_key}")

message = "This is RSA test message!"

encrypted_message = encrypt(message, public_key)
print(f"Зашифроване повідомлення: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, private_key)
print(f"Розшифроване повідомлення: {decrypted_message}")
