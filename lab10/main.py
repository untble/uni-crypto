import struct
import math


def md5(message):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    def F(X, Y, Z):
        return (X & Y) | ((~X) & Z)

    def G(X, Y, Z):
        return (X & Z) | (Y & (~Z))

    def H(X, Y, Z):
        return X ^ Y ^ Z

    def I(X, Y, Z):
        return Y ^ (X | (~Z))

    # Логічні зсуви
    def left_rotate(x, c):
        return (x << c) | (x >> (32 - c))

    original_message = message
    message = bytearray(message, 'utf-8')
    ml = 8 * len(original_message)
    message.append(0x80)
    while (len(message) * 8) % 512 != 448:
        message.append(0)

    message += struct.pack('<Q', ml)

    for chunk in struct.iter_unpack("<16I", message):
        X = list(chunk)
        AA, BB, CC, DD = A, B, C, D

        s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

        for i in range(64):
            if i < 16:
                k = i
            elif i < 32:
                k = (5 * i + 1) % 16
            elif i < 48:
                k = (3 * i + 5) % 16
            else:
                k = (7 * i) % 16

            F_value = F(BB, CC, DD) if i < 16 else G(BB, CC, DD) if i < 32 else H(BB, CC, DD) if i < 48 else I(BB, CC,
                                                                                                               DD)
            temp = (AA + F_value + X[k] + math.floor(2 ** 32 * abs(math.sin(i + 1)))) & 0xFFFFFFFF
            temp = (temp + left_rotate(BB, s[i]) + CC) & 0xFFFFFFFF
            AA, BB, CC, DD = DD, temp, BB, CC

        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(A, B, C, D)


message = "This is a secret message to test MD5!"
hash_value = md5(message)
print(f"Message: {message}")
print(f"MD5 Hash: {hash_value}")
