def multiply_by_02(byte):
    if byte & 0x80:  # Якщо старший біт дорівнює 1
        result = (byte << 1) ^ 0x1B
    else:
        result = byte << 1
    return result & 0xFF


def multiply_by_03(byte):
    # Множення на 03 зводиться до множення на 02 і потім додавання вихідного байту
    return multiply_by_02(byte) ^ byte


byte1 = 0xD4
result1 = multiply_by_02(byte1)
print("D4 * 02 =", hex(result1))

byte2 = 0xBF
result2 = multiply_by_03(byte2)
print("BF * 03 =", hex(result2))
