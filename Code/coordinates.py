import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Загрузите изображение
img = mpimg.imread('../Sours/Шаблон.jpg')

# Отобразите изображение
imgplot = plt.imshow(img)
plt.axis('off')  # отключить оси координат
plt.show()

# После отображения изображения вы сможете кликнуть по нему, и в консоли появятся координаты этой точки.
