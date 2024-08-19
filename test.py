from PIL import Image
start_image="Sours/Шаблон.jpg"
image = Image.open(start_image)

# Получаем ширину и высоту изображения
width, height = image.size

print("Ширина:", width)
print("Высота:", height)