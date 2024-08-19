from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta
import textwrap
import random
import tempfile
import shutil
import os

def del_all(folder_path):
    # Список для хранения имен удаленных файлов и папок
    deleted_items = []

    # Переберите все файлы и папки в папке
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Удалить файл
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Удалить папку и все её содержимое
            deleted_items.append(item)  # Добавить имя файла или папки в список удаленных элементов
        except Exception as e:
            print(f'Не удалось удалить {item_path}. Причина: {e}')

    # Вывести список удаленных файлов и папок
    '''print("Удалены следующие файлы и папки:")
    for item in deleted_items:
        print(item)
    print()'''
def del_img(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Файл {file} успешно удален.")
        else:
            print(f"Файл {file} не найден.")
def input_text(l,t,r,b,name_file, img):
    def ost():
        image = Image.open(img)
        draw = ImageDraw.Draw(image)

        # Автоматически переносим текст по ширине прямоугольника
        wrapper = textwrap.TextWrapper(width=34)  # Здесь можно настроить ширину
        word_list = wrapper.wrap(text)

        # Вычисляем высоту текста
        text_height = 0
        for line in word_list:
            width, height = draw.textbbox((0, 0), line, font=font)[2:]
            text_height += height

        # Определите начальное значение межстрочного интервала
        line_spacing = 15  # Измените это значение, чтобы увеличить или уменьшить интервал

        # Выравниваем текст по центру прямоугольника с учетом межстрочного интервала
        text_y = t
        for i, line in enumerate(word_list):
            width, height = draw.textbbox((0, 0), line, font=font)[2:]
            text_x = l + (r - l - width) / 2
            draw.text((text_x, text_y), line, fill="black", font=font)
            text_y += height + line_spacing  # Прибавляем интервал после каждой строки
        return image
    def random_date():
        start_date = datetime(1950, 1, 1)  # начальная дата
        end_date = datetime(2023, 12, 31)  # конечная дата
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date.strftime("%d.%m.%Y")
    def draw_vertical_text(image, text, left, top, right, bottom, color, font):
        image=Image.open(image)
        # Определяем координаты текста
        w = image.width
        t1x = top
        t1y = w - right
        t2x = bottom
        t2y = w - left

        # Поворачиваем изображение
        image = image.rotate(90, expand=True)

        # Рисуем прямоугольник
        draw = ImageDraw.Draw(image)

        # вставляем текст
        draw.text(((t1x + t2x) / 2, (t1y + t2y) / 2), text, fill=color, font=font, anchor="mm")

        # Поворачиваем изображение обратно
        image = image.rotate(-90, expand=True)

        return image

    # Устанавливаем размер и шрифт для текста
    font = ImageFont.truetype("Sours/ofont.ru_Courier New.ttf", 15)
    text=""
    if name_file=="Date":
        text = random_date()
        image=ost()
    elif name_file=="ser_1" or name_file=="ser_2":
        text=str(random.randint(10, 99))
        image = draw_vertical_text(img, text, l, t, r, b, "red", font)
        image.save("Sours/out/out.jpg")
        image = draw_vertical_text(img, text, l, t+335, r, b+335, "red", font)
    elif name_file=="number":
        text=str(random.randint(100000, 999999))
        image = draw_vertical_text(img, text, l, t, r, b, "red", font)
        image.save("Sours/out/out.jpg")
        image = draw_vertical_text(img, text, l, t+335, r, b+335, "red", font)
    else:
        # Открываем файл

        with open(name_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Выбираем случайную строку
        random_line = random.choice(lines)
        # Выводим случайную строку
        text = random_line.strip().upper()  # strip() удаляет символы новой строки и пробелы в начале и конце строки
        #print(text)
        image=ost()
    # Сохраняем изображение
    image.save("Sours/out/out.jpg")
    return text
def size(img):
    with Image.open(img) as image:
        image = image.convert("RGBA")  # Преобразование в формат RGBA, чтобы учитывать прозрачность
        width, height = image.size

    '''# Методы width и height:
    with Image.open("example.jpg") as img:
        width = img.width
        height = img.height
        print(f"Ширина: {width}, Высота: {height}")'''
    return width, height
def input_img(l, t, img, insert_img, output_path, img_save=None, r=None, b=None):
    # Открываем изображения
    background_image = Image.open(img)
    foreground_image = Image.open(insert_img).convert("RGBA")  # Открываем с сохранением прозрачности
    if r is not None and b is not None:
        # Изменяем размер вставляемого изображения до размеров области вставки
        foreground_image = foreground_image.resize((r - l, b - t))
        foreground_image.save(img_save)
    # Вставляем
    background_image.paste(foreground_image, (l, t), mask=foreground_image)
    # Сохраняем результат
    background_image.save(output_path)
    return output_path
def convert_to_grayscale(input_image_path, output_image_path):
    with Image.open(input_image_path) as image:
        gray_image = image.convert("L")
        gray_image.save(output_image_path)
    return output_image_path
def lt_corner(img,img_ins,bias=None):
    w, h = size(img)
    min_w, min_h = size(img_ins)
    if bias is not None:
        min_h-=bias
    l = random.randint(0, max(w-min_w,0))
    t = random.randint(0, max(h-min_h,0))
    if bias is not None:
        r=random.randint(l + min_w, max(w,l + min_w))
        b=random.randint(t + min_h, max(h,t + min_h))
        return l, t, r, b, img, img_ins
    return l,t,img,img_ins
def wh_corner(w,h,img,img_ins):
    width, height = size(img)
    min_w, min_h = w,h
    #print(width, height, min_w, min_h)
    l=0
    t=0
    if min_w<width:
        l = random.randint(0, max(width-min_w,0))
    if min_h<height:
        t = random.randint(0, max(height-min_h,0))
    #print(l,t,img,img_ins)
    return l,t,img,img_ins
def crop(img,img_crop):
    # Случайно обрезаем копию изображения znak
    left, upper,right, lower, img_crop, img= lt_corner(img_crop,img,365)
    # Создаем копию изображения znak
    copied_image = Image.open(img_crop).convert("RGBA")
    copied_image = copied_image.crop((left, upper, right, lower))
    # Сохраняем скопированное и обрезанное изображение во временный файл
    temp_image_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    copied_image.save(temp_image_path.name)
    return temp_image_path
def rotation(img, out_img):
    # Открываем изображение в формате JPG
    img = Image.open(img)
    # Создаем новое изображение с прозрачным фоном
    new_img = Image.new("RGBA", img.size, (255, 255, 255, 0))
    # Налагаем изначальное изображение на новое изображение
    new_img.paste(img, (0, 0))
    # Поворачиваем изображение
    angle = random.uniform(0, 360)
    rotated_img = new_img.rotate(angle, resample=Image.BICUBIC, expand=True)
    # Создаем новое изображение с прозрачным фоном
    final_img = Image.new("RGBA", rotated_img.size, (255, 255, 255, 0))
    # Налагаем повернутое изображение на новое изображение
    final_img.paste(rotated_img, (0, 0), rotated_img)
    # Сохраняем перевернутое изображение в формате PNG
    final_img.save(out_img)
    # Получаем описывающий прямоугольник
    bbox = final_img.getbbox()
    # Выводим длину и ширину прямоугольника
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    '''# Отображаем изображение и прямоугольник
    fig, ax = plt.subplots()
    ax.imshow(final_img)
    rect = plt.Rectangle((bbox[0], bbox[1]), width, height, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.show()'''
    return out_img, width, height
def new_line(path,line):
    with open(path, 'a',encoding='utf-8') as file:
        file.write(line+"\n")
def main(save_text,save_image,image_png):
    # Открываем изображение
    del_all("Sours/out")
    start_image="Sours/Шаблон.jpg"
    image_jpg = "Sours/out/out.jpg"

    image_rotate=""
    random_file = random.choice(os.listdir("Sours/Faces"))
    znak="Sours/знак_1.png"

    new_line(save_text, input_text(105, 75, 475, 145, "Sours/Text/passport_issued.txt", start_image))
    new_line(save_text, input_text(290, 160, 470, 175, "Sours/Text/code.txt", image_jpg))
    new_line(save_text,input_text(105,160,195,175,"Date", image_jpg))
    new_line(save_text,input_text(350,520,430,530, "Date", image_jpg))
    new_line(save_text, input_text(200, 520, 245, 530, "Sours/Text/pol.txt", image_jpg))
    new_line(save_text, input_text(215, 410, 470, 450, "Sours/Text/sername.txt", image_jpg))
    new_line(save_text, input_text(215, 465, 470, 480, "Sours/Text/name.txt", image_jpg))
    new_line(save_text, input_text(215, 490, 470, 500, "Sours/Text/father_name.txt", image_jpg))
    new_line(save_text, input_text(215, 545, 470, 620, "Sours/Text/place_of_birth.txt", image_jpg))
    ser_1=input_text(490,90,505,145, "ser_1", image_jpg)
    ser_2=input_text(490,145,505,175, "ser_2", image_jpg)
    number=input_text(490,175,505,285, "number", image_jpg)
    new_line(save_text,ser_1)
    new_line(save_text,ser_2)
    new_line(save_text,number)
    start_image=input_img(33, 447, image_jpg, os.path.join("Sours/Faces", random_file), image_png, save_image, 168, 617)  # первое изображение

    # ВОДЯНОЙ ЗНАК
    if random.choice([True, False]):
        #print("ВОДЯНОЙ ЗНАК")
        image_png = input_img(0, 365, start_image, crop(start_image, znak), image_png)
    # СЕРЫЙ ЦВЕТ
    if random.choice([True, False]):
        #print("СЕРЫЙ ЦВЕТ")
        # серое фото:
        convert_to_grayscale(save_image, save_image)
        if os.path.exists(image_png):
            image_png = convert_to_grayscale(image_png, image_png)
        else:
            image_png = convert_to_grayscale(start_image, image_png)
    # ПОВОРОТ
    if random.choice([True, False]):
        #print("ПОВОРОТ")
        if os.path.exists(image_png):
            image_rotate, w, h = rotation(image_png, image_png)
        else:
            image_rotate, w, h = rotation(start_image, image_png)
    # ВСТАВКА ПАСПОРТА
    if random.choice([True, False]):
        substrate = random.choice(["Sours/A4_gorizontal.png", "Sours/A4_vertical.png"])
        #print("ВСТАВКА ПАСПОРТА")
        if os.path.exists(image_rotate):
            '''l, t, img, img_ins = wh_corner(w, h,substrate, image_rotate)
            image_png = input_img(l, t, img, img_ins, image_png)'''
        else:
            if os.path.exists(image_png):
                l, t, img, img_ins = lt_corner(substrate, image_png)
                image_png = input_img(l, t, img, img_ins, image_png)
            else:
                l, t, img, img_ins = lt_corner(substrate, start_image)
                image_png = input_img(l, t, img, img_ins, image_png)

if __name__=="__main__":
    #path="Output"
    path="Output_chek"
    #path = r"C:\Users\КИТ\PycharmProjects\Diplom\Output"
    #path = r"C:\Users\КИТ\PycharmProjects\Diplom\Output_chek"
    if os.path.exists(path):
        del_all(path)
    n=20
    '''for i in range(1,n+1):
        folder=path+f"/{i}"
        os.makedirs(folder,exist_ok=True)
        save_text = folder+"/text.txt"
        save_image= folder+"/face.png"
        image_png= folder+"/image.png"

        #save_text =f"Output/output_{i}.txt"
        #save_image =f"Output/face_{i}.png"
        #image_png = f"Output/output_{i}.png"
        main(save_text,save_image,image_png)'''
    name_dir_txt = "text"
    name_dir_img = "image"
    name_dir_face = "face"
    os.makedirs(f"{path}/{name_dir_txt}", exist_ok=True)
    os.makedirs(f"{path}/{name_dir_img}", exist_ok=True)
    os.makedirs(f"{path}/{name_dir_face}", exist_ok=True)
    for i in range(1, n + 1):
        save_text = f"{path}/{name_dir_txt}/text_{i}.txt"
        save_image = f"{path}/{name_dir_img}/image_{i}.png"
        save_face = f"{path}/{name_dir_face}/face_{i}.png"
        print(save_text)
        print(save_face)
        print(save_image)
        main(save_text, save_face, save_image)

