import hashlib
import random


def is_prime(num, k=5):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    s, d = 0, num - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True


def generate_large_prime(bit_length):
    while True:
        num = random.getrandbits(bit_length)
        if is_prime(num):
            return num


def find_generator(p):
    for g in range(2, p):
        if pow(g, (p - 1) // 2, p) != 1 and pow(g, p - 1, p) == 1:
            return g


def generate_elgamal_params():
    bit_length = 1024
    p = generate_large_prime(bit_length)
    g = find_generator(p)

    return p, g


p, g = generate_elgamal_params()


def generate_keypair(p, g):
    x = random.randint(1, p - 1)
    y = pow(g, x, p)
    return x, y


def sign(message, p, g, x):
    k = random.randint(1, p - 2)
    r = pow(g, k, p)
    m_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    s = (pow(k, -1, p - 1) * (m_hash + x * r)) % (p - 1)
    return r, s


def verify(message, signature, p, g, y):
    r, s = signature
    if 0 < r < p and 0 < s < p - 1:
        m_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        w = pow(s, -1, p - 1)
        u1 = (m_hash * w) % (p - 1)
        u2 = (r * w) % (p - 1)
        v = (pow(g, u1, p) * pow(y, u2, p)) % p
        return v == r
    return False


private_key, public_key = generate_keypair(p, g)
print("Private key:", private_key)
print("Public key:", public_key)

message_to_sign = "TEST"
signature = sign(message_to_sign, p, g, private_key)
print("Signature:", signature)

verification_result = verify(message_to_sign, signature, p, g, public_key)
print("Verification Result:", verification_result)
