from itertools import cycle

alp = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
key = "віженервіженервіжене"


def encode(text, key_text):
    def f(arg):
        return alp[(alp.index(arg[0]) + alp.index(arg[1])) % len(alp)]

    return "".join(map(f, zip(text, cycle(key_text))))


def decode(text, key_text):
    def f(arg):
        return alp[(alp.index(arg[0]) - alp.index(arg[1]) % 33) % 33]

    return "".join(map(f, zip(text, cycle(key_text))))


result = encode(input("Введіть текст: ").encode('utf-8').decode('utf-8'), key)
print(f"Зашифрований текст: {result}")
print(f"Розшифрований текст: {decode(result, key)}")
