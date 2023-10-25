def gcdex(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


a = 612
b = 342
d, x, y = gcdex(a, b)
print(f'd = {d}')
print(f'x = {x}')
print(f'y = {y}')