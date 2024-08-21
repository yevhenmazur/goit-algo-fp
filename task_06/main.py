'''
Написати програму на Python, яка використовує два підходи — жадібний алгоритм
та алгоритм динамічного програмування для розв’язання задачі вибору їжі з
найбільшою сумарною калорійністю в межах обмеженого бюджету.
Дані про їжу представлені у вигляді словника items
'''


def greedy_algorithm(items, budget):
    '''Жадібний алгоритм'''
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for item, details in sorted_items:
        cost = details['cost']
        calories = details['calories']

        if remaining_budget >= cost:
            chosen_items.append(item)
            total_calories += calories
            remaining_budget -= cost

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    '''Підхід з динамічним програмуванням'''
    item_names = list(items.keys())
    n = len(item_names)

    # Створюю таблицю DP
    dp_table = [[0 for x in range(budget + 1)] for y in range(n + 1)]

    # Створюю таблицю для обраних страв
    selected_dishes = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']

        for j in range(budget + 1):
            if cost <= j:
                if dp_table[i-1][j-cost] + calories > dp_table[i-1][j]:
                    dp_table[i][j] = dp_table[i-1][j-cost] + calories
                    selected_dishes[i][j] = selected_dishes[i -
                                                            1][j-cost] + [name]
                else:
                    dp_table[i][j] = dp_table[i-1][j]
                    selected_dishes[i][j] = selected_dishes[i-1][j]
            else:
                dp_table[i][j] = dp_table[i-1][j]
                selected_dishes[i][j] = selected_dishes[i-1][j]

    max_cal = dp_table[n][budget]
    chosen_items = selected_dishes[n][budget]

    return max_cal, budget, chosen_items


if __name__ == '__main__':

    budget = 100

    # Словник із продуктами
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("\nРезультати жадібного алгоритму\n")
    print(f"Калорій: {greedy_result[0]}\nБюджету використано: {
          greedy_result[1]} з {budget}\nВибрані продукти: {greedy_result[2]}")

    print("\nРезультат ДП\n")
    print(f"Калорій: {dp_result[0]}\nБюджету використано: {
          dp_result[1]} з {budget}\nВибрані продукти: {dp_result[2]}")
