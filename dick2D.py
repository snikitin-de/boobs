import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def save_dick():
    # Генерация расы и цвета кожи
    races = {
        'White'   : '#ffdbaf',
        'Irish'   : '#fff2e2',
        'Black'   : '#756046',
        'African' : '#443421',
        'Asian'   : '#ffe8b2',
        'Hispanic': '#edb86f',
        'Indian'  : '#997138',
    }

    racename, racevalue = random.choice(list(races.items()))

    # Генерация размеров
    bsize = random.randint(25, 80)            # размер яичек
    girth = random.randint(25, bsize)         # окружность
    length = random.randint(150, 450)         # длина
    xoffset = 0 - (length / 2)
    head_color = 'pink'

    # Отладочный вывод
    print('Race:', racename)
    print('Ball size:', bsize)
    print('Girth:', girth)
    print('Length:', length)

    # Подготовка холста
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_facecolor('black')

    # Яички
    left_ball = patches.Circle((xoffset, -bsize * 0.8), bsize, color=racevalue)
    right_ball = patches.Circle((xoffset, bsize * 0.8), bsize, color=racevalue)

    # Ствол
    shaft = patches.Rectangle((xoffset, -girth), length, girth * 2, color=racevalue)

    # Головка
    head = patches.Wedge((xoffset + length, 0), girth, 270, 90, color=head_color)

    # Добавление фигур
    for shape in [left_ball, right_ball, shaft, head]:
        ax.add_patch(shape)

    # Границы и сохранение
    ax.set_xlim(xoffset - bsize, xoffset + length + girth + 20)
    ax.set_ylim(-bsize * 2, bsize * 2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Сохранение в файл
    plt.savefig(r'.\dick.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
