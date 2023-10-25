def inverse_element_2(a, n):
    if n <= 1:
        return None
    p = n
    if p <= 1:
        return None
    if p > 1:
        return pow(a, p - 2, p)


a = 5
n = 18
result = inverse_element_2(a, n)

if result is not None:
    print(f"The multiplicative inverse of {a} modulo {n} is {result}")
else:
    print(f"The multiplicative inverse of {a} modulo {n} does not exist.")