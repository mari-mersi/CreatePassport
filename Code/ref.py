# Открываем файл place_of_birth.txt с явным указанием кодировки
with open('../Sours/Text/place_of_birth.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('../Sours/Text/place_of_birth.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        # Добавляем "г. " перед каждым городом и записываем обратно в файл
        f.write(f"г. {line}")

print("Готово. Проверьте файл place_of_birth.txt для результ.")
