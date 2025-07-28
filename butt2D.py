import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Arc

def save_butt():
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    color = 'black'
    width = 10

    # Левая половина — более округлая, без "плеч"
    verts_left = [
        (-1.1, 3.5),       # талия
        (-1.3, 2.8),       # верхний бок
        (-1.25, 2.0),      # мягкий изгиб
        (-1.15, 1.3),      # центр ягодицы
        (-1.0, 1.0),       # низ ягодицы
        (-1.05, -1.4)
    ]
    codes = [Path.MOVETO] + [Path.CURVE3]*4 + [Path.LINETO]

    # Правая половина — симметрично
    verts_right = [(x * -1, y) for x, y in verts_left]

    # Межъягодичная линия — глубокая S-образная выемка
    verts_middle = [
        (0.0, 1.4),
        (-0.1, 1.1),
        (0.0, 0.75),
        (0.1, 0.3),
        (0.0, -1.4)
    ]
    codes_middle = [Path.MOVETO] + [Path.CURVE3]*3 + [Path.LINETO]

    # Основной контур
    for verts in [verts_left, verts_right, verts_middle]:
        path = Path(verts, codes if verts is not verts_middle else codes_middle)
        patch = PathPatch(path, edgecolor=color, facecolor='none', linewidth=width, capstyle='round')
        ax.add_patch(patch)

    # Нижние дуги под попой — поднимаем чуть выше
    arc_left = Arc((-0.75, 1.1), 0.6, 0.3, angle=0, theta1=210, theta2=330,
                edgecolor=color, linewidth=width)
    arc_right = Arc((0.75, 1.1), 0.6, 0.3, angle=0, theta1=210, theta2=330,
                    edgecolor=color, linewidth=width)
    ax.add_patch(arc_left)
    ax.add_patch(arc_right)

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 4)

    plt.savefig(r'.\butt.png', dpi=300, bbox_inches='tight', transparent=True)
