from turtle import *
import random, os

# Настройка окна
os.system('mode con: cols=50 lines=10')

# Случайный выбор цвета кожи
skin_tones = {
    'Black': '#443421',
    'White': '#ffdbaf',
    'Irish': '#fff2e2',
    'African': '#756046',
    'Asian': '#ffe8b2',
    'Hispanic': '#edb86f',
    'Indian': '#997138',
}

race_name, skin_color = random.choice(list(skin_tones.items()))
breast_size = random.randint(60, 100)  # Радиус груди
nipple_size = breast_size // 4         # Радиус соска
spacing = -10                          # Отрицательное значение для небольшого наложения

# Вывод параметров
print('Race:', race_name)
print('Breast size:', breast_size)
print('Nipple size:', nipple_size)

# Настройка окна черепашки
hideturtle()
screen_width = breast_size * 2 * 2 + 100  # две груди
screen_height = breast_size * 2 + 100
setup(screen_width, screen_height)
title('Boobs Window')
speed(10)
bgcolor('black')

# Функция рисования груди
def draw_breast(x, y):
    penup()
    goto(x, y)
    pendown()
    color(skin_color)
    begin_fill()
    circle(breast_size)
    end_fill()

    # Сосок
    penup()
    goto(x, y + breast_size - nipple_size)
    pendown()
    color('brown')
    begin_fill()
    circle(nipple_size)
    end_fill()

# Центрирование
start_x = -breast_size
start_y = -breast_size // 2

# Рисуем левую грудь
draw_breast(start_x, start_y)

# Рисуем правую грудь (впритык)
draw_breast(start_x + breast_size * 2 + spacing, start_y)

print('Complete.')
done()
