import random
import sympy


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


def find_primitive_root(p):
    for g in range(2, p):
        if sympy.ntheory.is_primitive_root(g, p):
            return g


def generate_params():
    while True:
        p_candidate = random.randint(2 ** 10, 2 ** 12)
        if is_prime(p_candidate):
            g_candidate = find_primitive_root(p_candidate)
            if g_candidate:
                return p_candidate, g_candidate


def generate_keys():
    p, g = generate_params()
    a = random.randint(2, p - 2)
    h = pow(g, a, p)
    return p, g, a, h


def encrypt(message, p, g, h):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(h, k, p)
    c2 = (s * message) % p
    return c1, c2


def decrypt(c1, c2, p, a):
    s = pow(c1, a, p)
    s_inv = sympy.mod_inverse(s, p)
    message = (c2 * s_inv) % p
    return message


if __name__ == "__main__":
    p, g, a, h = generate_keys()
    message = 472

    c1, c2 = encrypt(message, p, g, h)
    decrypted_message = decrypt(c1, c2, p, a)

    print("Original message:", message)
    print("Encrypted message:", (c1, c2))
    print("Decrypted message:", decrypted_message)
