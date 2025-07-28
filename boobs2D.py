import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def save_breast():
    # Цвета кожи
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
    breast_size = random.randint(60, 100)
    nipple_size = breast_size // 4
    spacing = -10

    print('Race:', race_name)
    print('Breast size:', breast_size)
    print('Nipple size:', nipple_size)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    plt.axis('off')

    left_x = breast_size + 10
    right_x = left_x + breast_size * 2 + spacing
    center_y = breast_size + 10

    def draw_breast(center_x, center_y):
        breast = patches.Circle((center_x, center_y), breast_size,
                                facecolor=skin_color, edgecolor='none')
        ax.add_patch(breast)
        nipple = patches.Circle((center_x, center_y),
                                nipple_size, facecolor='brown', edgecolor='none')
        ax.add_patch(nipple)

    draw_breast(left_x, center_y)
    draw_breast(right_x, center_y)

    margin = 20
    plt.xlim(0, right_x + breast_size + margin)
    plt.ylim(0, center_y + breast_size + margin)

    path = r'.\boobs.png'
    plt.savefig(path, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()

    print(f'Saved to {path}')
