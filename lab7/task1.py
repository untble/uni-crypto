import random


def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y & 1:
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result


def is_witness(a, n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    x = power(a, d, n)

    if x == 1 or x == n - 1:
        return False

    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False

    return True


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True, 1.0

    if n % 2 == 0 or n == 1:
        return False, 0.0

    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_witness(a, n):
            return False, 0.0

    return True, 1.0 - 1.0 / (2 ** k)


n = int(input("Введіть натуральне непарне число n (>3): "))
k = int(input("Введіть кількість раундів k: "))

is_prime, probability = miller_rabin_test(n, k)

if is_prime:
    print(f"{n} можливо просте з ймовірністю {probability:.5f}")
else:
    print(f"{n} складене")