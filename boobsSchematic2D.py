import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 17)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

def draw_breast(center_x, center_y):
    # Грудь (контур)
    breast = patches.Circle((center_x, center_y), 4, color='peachpuff', alpha=0.8)
    ax.add_patch(breast)

    # Ареола
    areola = patches.Circle((center_x, center_y), 1.2, color='lightcoral')
    ax.add_patch(areola)

    # Сосок
    nipple = patches.Circle((center_x, center_y), 0.3, color='brown')
    ax.add_patch(nipple)

    # Млечные протоки (лучи от центра)
    for angle in range(0, 360, 30):
        x_end = center_x + 2.5 * 0.95 * np.cos(np.radians(angle))
        y_end = center_y + 2.5 * 0.95 * np.sin(np.radians(angle))
        ax.plot([center_x, x_end], [center_y, y_end], color='darkred', linewidth=1.5)

    # Дольки молочной железы (окружности вокруг соска)
    for angle in range(0, 360, 60):
        x = center_x + 2 * np.cos(np.radians(angle))
        y = center_y + 2 * np.sin(np.radians(angle))
        lobe = patches.Circle((x, y), 0.6, color='mistyrose')
        ax.add_patch(lobe)

# Рисуем две груди дальше друг от друга
draw_breast(4, 5)
draw_breast(13, 5)

plt.show()