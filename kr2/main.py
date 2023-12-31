from sympy import Point

# Відомі параметри еліптичної кривої та базової точки
p = 127
G = Point(95, 65)  # Результат додавання P і Q

# Закритий ключ та відкритий ключ
d_A = 37  # Приклад значення закритого ключа
Q_A = d_A * G

# Повідомлення для шифрування
P = Point(56, 7)  # Приклад значення повідомлення P

# Етап шифрування
k = 73  # Випадкове число взято статично, але ВАЖЛИВО, щоб воно було різне у реальних проектах!!!
C_1 = k * G
C_2 = P + k * Q_A

# Етап розшифрування
neg_d_A = -d_A % p  # Обчислення оберненого за модулем від d_A

# Обчислення -d_A * C_1
decryption_step1 = neg_d_A * C_1

# Обчислення P + (-d_A * k * G)
decrypted_P = P + decryption_step1

# Виведення результатів
print("Ciphertext C_1 ---> ", C_1)
print("Ciphertext C_2 ---> ", C_2)
print("Decrypted Point P ---> ", decrypted_P)