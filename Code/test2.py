from PIL import Image, ImageDraw

# Создаем изображение белого цвета размером 100x100
image = Image.new("RGB", (100, 100), "white")

# Создаем объект ImageDraw для рисования
draw = ImageDraw.Draw(image)

# Рисуем красный квадрат на изображении
draw.rectangle([10, 10, 90, 90], fill="red")

# Сохраняем изображение в файл
image.save("example_image.png")

print("Pillow работает успешно!")
