import random
import math


def is_prime(n, k=5):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p


def primitive_root(p):
    for g in range(2, p):
        if math.gcd(g, p) == 1:
            return g


def diffie_hellman_key_exchange():
    p = generate_prime(16)
    g = primitive_root(p)

    private_key_a = random.randint(2, p - 1)
    private_key_b = random.randint(2, p - 1)

    public_key_a = pow(g, private_key_a, p)
    public_key_b = pow(g, private_key_b, p)

    shared_key_a = pow(public_key_b, private_key_a, p)
    shared_key_b = pow(public_key_a, private_key_b, p)

    print("p:", p)
    print("g:", g)
    print("Open key A:", public_key_a)
    print("Open key B:", public_key_b)
    print("Shared key A:", shared_key_a)
    print("Shared key B:", shared_key_b)


if __name__ == "__main__":
    diffie_hellman_key_exchange()