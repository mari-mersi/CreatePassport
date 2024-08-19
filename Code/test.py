def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

text=["Иван","Иванов",30,"Инженер"]

# Пример использования
data = {
    "Имя": text[0],
    "Фамилия": text[1],
    "Возраст": text[2],
    "Профессия": text[3]
}
file_path = "output.txt"
write_to_file(file_path, data)

