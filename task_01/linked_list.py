class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr is None:
            return
        prev.next = curr.next
        curr = None

    def search_element(self, data: int) -> Node | None:
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def reverse_list(self):
        '''Виконує реверсування однозв'язного списку'''
        prev, curr = None, self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        return self.head

    def sort_list(self):
        '''Сортує однозв'язний список вставками'''
        if not self.head or not self.head.next:
            return

        sorted_head = None

        curr = self.head
        while curr:
            next_node = curr.next

            # Вставляємо curr у відсортовану частину списку
            sorted_head = self.insert_sorted(sorted_head, curr)

            curr = next_node

        self.head = sorted_head

    def insert_sorted(self, sorted_head, node_to_insert):
        if not sorted_head or node_to_insert.data <= sorted_head.data:
            node_to_insert.next = sorted_head
            return node_to_insert

        curr = sorted_head
        while curr.next and curr.next.data < node_to_insert.data:
            curr = curr.next

        node_to_insert.next = curr.next
        curr.next = node_to_insert

        return sorted_head
