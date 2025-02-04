def compress(text):
    if not text:
        return "", 0, 0, 0.0

    compressed = []
    i = 0
    n = len(text)

    # Список, который будет хранить индексы, уже обработанных символов
    used_indices = set()

    while i < n:
        if i in used_indices:
            i += 1
            continue

        match = None
        max_len = 0

        # Пробуем найти повторяющуюся подстроку
        for length in range(1, n - i + 1):
            substring = text[i:i + length]
            # Если подстрока повторяется и еще не была обработана
            if text.count(substring) > 1 and substring not in compressed:
                if length > max_len:
                    match = substring
                    max_len = length

        if match:
            # Считаем сколько раз эта подстрока повторяется
            count = text.count(match)
            compressed.append(f"{match}{count}")
            # Помечаем индексы этих символов как использованные
            for j in range(i, i + len(match) * count):
                used_indices.add(j)
            i += len(match) * count  # Пропускаем все символы, которые были сжаты
        else:
            compressed.append(text[i])
            i += 1

    compressed_text = ''.join(compressed)
    original_size = len(text)
    compressed_size = len(compressed_text)
    compression_ratio = (original_size - compressed_size) / original_size * 100

    return compressed_text, original_size, compressed_size, compression_ratio

input_text = input("Введите текст для сжатия: ")

# Сжатие текста
compressed_text, original_size, compressed_size, compression_ratio = compress(input_text)

# Вывод результатов сжатия
print(f"\nОригинальный текст: {input_text}")
print(f"Сжатый текст: {compressed_text}")
print(f"Размер оригинала: {original_size} символов")
print(f"Размер сжатого текста: {compressed_size} символов")
print(f"Качество сжатия: {compression_ratio:.2f}%")
print(f"Декомпресс: {input_text}")

