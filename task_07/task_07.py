'''
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків,
обчислює суми чисел, які випадають на кубиках,
і визначає ймовірність кожної можливої суми.
'''

import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    rolls_count = 0
    probabilities = {}
    sum_counts = {}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = str(die1 + die2)

        if roll_sum in sum_counts:
            sum_counts[roll_sum] += 1
        else:
            sum_counts[roll_sum] = 1

        rolls_count += 1

    # Збираю дані про імовірності випадінь в один словник
    for roll_sum, count in sum_counts.items():
        probability = count / rolls_count
        probabilities[roll_sum] = probability
        sorted_probabilities = dict(
            sorted(probabilities.items(), key=lambda item: int(item[0])))

    return sorted_probabilities


def plot_probabilities(probabilities, ax, rolls_count):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    ax.bar(sums, probs, tick_label=sums)
    ax.set_xlabel('Сума чисел на кубиках')
    ax.set_ylabel('Ймовірність')
    ax.set_title(f'{rolls_count} кидків кубиків')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        ax.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')


if __name__ == "__main__":
    accuracies = [100, 1000, 10000, 100000]
    num_plots = len(accuracies)

    fig, axes = plt.subplots(nrows=(num_plots + 1) //
                             2, ncols=2, figsize=(14, 8))
    axes = axes.flatten()  # для простого індексування

    for i, accuracy in enumerate(accuracies):
        probabilities = simulate_dice_rolls(accuracy)
        plot_probabilities(probabilities, axes[i], accuracies[i])

    # Видаляємо порожні підмножини (якщо їх більше, ніж потрібно)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
