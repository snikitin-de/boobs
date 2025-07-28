import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Грудные параметры
breast_radius = 8
breast_depth = 4.5
spacing = 9
u_res, v_res = 120, 120

# Параметры соска
nipple_radius = 1.2
nipple_height = 0.8

# Сетка груди (глубже, округлее)
u = np.linspace(0, 2 * np.pi, u_res)
v = np.linspace(0, 2/3 * np.pi, v_res)
u, v = np.meshgrid(u, v)
x_base = breast_radius * np.cos(u) * np.sin(v)
y_base = breast_radius * np.sin(u) * np.sin(v)
z_base = breast_depth * np.cos(v)

# Поворот вперёд (по X)
angle_x = np.radians(35)
Rx = np.array([
    [1, 0, 0],
    [0, np.cos(angle_x), -np.sin(angle_x)],
    [0, np.sin(angle_x),  np.cos(angle_x)]
])

# Центр верхушки груди (до поворота)
center_idx = (0, 0)
center_local = np.array([
    x_base[center_idx],
    y_base[center_idx],
    z_base[center_idx]
])
center_l = Rx @ (center_local + np.array([-spacing, 0, 0]))
center_r = Rx @ (center_local + np.array([ spacing, 0, 0]))

# Левая и правая грудь
xyz_l = np.stack((x_base - spacing, y_base, z_base), axis=-1) @ Rx.T
xyz_r = np.stack((x_base + spacing, y_base, z_base), axis=-1) @ Rx.T
x_l, y_l, z_l = xyz_l[..., 0], xyz_l[..., 1], xyz_l[..., 2]
x_r, y_r, z_r = xyz_r[..., 0], xyz_r[..., 1], xyz_r[..., 2]

# Построение
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_l, y_l, z_l, color='#e3b8a5', linewidth=0, antialiased=True)
ax.plot_surface(x_r, y_r, z_r, color='#e3b8a5', linewidth=0, antialiased=True)

# Функция: создаёт выпуклый сосок
def add_nipple(center, R, color):
    # Параметры купола (в полярных координатах)
    theta = np.linspace(0, 2 * np.pi, 60)
    r = np.linspace(0, nipple_radius, 30)
    theta, r = np.meshgrid(theta, r)

    # Купол в локальных координатах
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.sqrt(np.maximum(0, nipple_height**2 - (r**2)))  # полусфера по уравнению

    # Преобразование в глобальные координаты
    points = np.stack((x, y, z), axis=-1).reshape(-1, 3) @ R.T
    points += center
    x_, y_, z_ = points[:, 0], points[:, 1], points[:, 2]
    ax.plot_trisurf(x_, y_, z_, color=color)

# Добавление сосков
add_nipple(center_l, Rx, '#a0755a')
add_nipple(center_r, Rx, '#a0755a')

# Отображение
ax.view_init(elev=10, azim=15)
ax.set_xlim(-25, 25)
ax.set_ylim(-10, 10)
ax.set_zlim(-5, 14)
ax.axis('off')
plt.title("Соски с объёмом и анатомическим положением", pad=20)
plt.tight_layout()
plt.show()



