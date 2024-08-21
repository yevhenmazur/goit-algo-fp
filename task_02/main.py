'''Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії'''

import matplotlib.pyplot as plt
import numpy as np


def draw_branch(ax, x, y, angle, size, depth):
    if depth == 0:
        return

    # Обчислюю вершини квадрата
    x1 = x + size * np.cos(angle)
    y1 = y + size * np.sin(angle)
    x2 = x1 - size * np.sin(angle)
    y2 = y1 + size * np.cos(angle)
    x3 = x - size * np.sin(angle)
    y3 = y + size * np.cos(angle)

    # і центр квадрата
    center_x = (x + x1 + x2 + x3) / 4
    center_y = (y + y1 + y2 + y3) / 4

    # З'єдную центр батьківського квадрата з дочірнім
    ax.plot([x, center_x], [y, center_y], color='green')

    # Обчислюю параметри наступних гілок
    new_size = size * np.sqrt(2) / 2
    new_angle1 = angle + np.pi / 4
    new_angle2 = angle - np.pi / 4

    # Рекурсивно малюю гілки
    draw_branch(ax, center_x, center_y, new_angle1, new_size, depth - 1)
    draw_branch(ax, center_x, center_y, new_angle2, new_size, depth - 1)


# Налаштування вікна для малювання
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Початкові умови
initial_x = 0
initial_y = 0
initial_size = 10
initial_angle = np.pi / 4

while True:
    depth = input("Введіть глибину рекурсії (2 - 15) >>> ")
    try:
        depth = int(depth)
    except ValueError:
        print('Рівень рекурсії має бути цілим числом')
        continue
    if 2 <= depth <= 15:
        break
    else:
        print('Від 2 до 15 будь ласка')


draw_branch(ax, initial_x, initial_y, initial_angle, initial_size, depth)

plt.show()
