def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None


def encrypt(message, a, s, n):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            char_value = ord(char) - ord('a')
            encrypted_char_value = (a * char_value + 3) % n
            encrypted_char = chr(encrypted_char_value + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(ciphertext, a, s, n):
    a_inverse = mod_inverse(a, n)
    s_inverse = (-a_inverse * s) % n
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            char_value = ord(char) - ord('a')
            decrypted_char_value = (a_inverse * (char_value - s_inverse)) % n - 1
            decrypted_char = chr(decrypted_char_value + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


if __name__ == "__main__":
    n = 26
    a = 7
    s = 2

    plaintext = "vitalii dvorskyi"

    encrypted_text = encrypt(plaintext, a, s, n)
    print("Зашифрований текст:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, a, s, n)
    print("Розшифрований текст:", decrypted_text)
