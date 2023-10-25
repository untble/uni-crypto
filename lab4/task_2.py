def gcdex(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inverse_element(a, n):
    d, x, y = gcdex(a, n)
    if d == 1:
        return x % n
    else:
        return None


a = 5
n = 18
result = inverse_element(5, 18)

if result is not None:
    print(f"The multiplicative inverse of {a} modulo {n} is {result}")
else:
    print(f"The multiplicative inverse of {a} modulo {n} does not exist.")