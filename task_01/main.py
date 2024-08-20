from linked_list import LinkedList


def merge_lists(llist1, llist2):
    curr1 = llist1.head
    curr2 = llist2.head
    res = LinkedList()

    while curr1 and curr2:
        if curr1.data < curr2.data:
            res.insert_at_end(curr1.data)
            curr1 = curr1.next
        else:
            res.insert_at_end(curr2.data)
            curr2 = curr2.next

    # Додаю, якщо щось лишилося після ітеративного злиття
    while curr1:
        res.insert_at_end(curr1.data)
        curr1 = curr1.next

    while curr2:
        res.insert_at_end(curr2.data)
        curr2 = curr2.next

    return res


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Реверсую список
llist.reverse_list()
print("\nСписок після реверсування")
llist.print_list()

# Сортую список
llist.sort_list()
print("\nСписок після сортування")
llist.print_list()

# Ініціалізую та наповнюю другий список
llist2 = LinkedList()
for i in range(1, 10):
    llist2.insert_at_end(i)

# Зливаю списки
merged_llist = merge_lists(llist, llist2)
print("\nСписок після злиття з іншим")
merged_llist.print_list()
