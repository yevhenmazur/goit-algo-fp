import uuid
import heapq
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
       # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, window_title="Graph Visualization"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    fig = plt.figure(figsize=(8, 5))
    # fig.canvas.set_window_title(window_title)
    fig.canvas.manager.set_window_title(window_title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    '''Реалізація побудови дерева з бінарної купи'''
    if index >= len(heap):
        return None

    root = Node(heap[index])

    root.left = build_heap_tree(heap, 2 * index + 1)
    root.right = build_heap_tree(heap, 2 * index + 2)

    return root


def generate_color(step, total_steps):
    '''Обраховує відтінок кольору, відповідно до послідовності його проходження'''
    base_color = [50, 168, 127]
    end_color = [237, 74, 74]

    r_mod_factor = (end_color[0] - base_color[0]) / total_steps * step
    g_mod_factor = (end_color[1] - base_color[1]) / total_steps * step
    b_mod_factor = (end_color[2] - base_color[2]) / total_steps * step

    new_color = [
        int(base_color[0] + r_mod_factor),
        int(base_color[1] + g_mod_factor),
        int(base_color[2] + b_mod_factor)
    ]

    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root):
    '''Реалізація алгоритму DFS'''
    total_steps = count_nodes(root)
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()

        if node and node.id not in visited:
            visited.add(node.id)

            # Призначаємо колір відповідно до кроку
            node.color = generate_color(step, total_steps)
            colors[node.id] = node.color
            step += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return colors


def bfs_visualize(root):
    '''Реалізація алгоритму BFS'''
    total_steps = count_nodes(root)
    visited, queue = set(), deque([root])
    colors = {}
    step = 0

    while queue:
        node = queue.popleft()

        if node and node.id not in visited:
            visited.add(node.id)

            # Призначаємо колір відповідно до кроку
            node.color = generate_color(step, total_steps)
            colors[node.id] = node.color
            step += 1

            # Додаємо дочірні вузли до черги (спочатку лівий, потім правий)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == '__main__':
    # Є у нас бінарна купа у вигляді списку
    heap_list = [1, 3, 5, 7, 9, 2, 10, 12, 15, 21, 8, 23, 57, 30]
    heapq.heapify(heap_list)
    print(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Обрахунок кількості кроків (вузлів)
    total_steps = count_nodes(heap_tree_root)

    # DFS візуалізація
    dfs_colors = dfs_visualize(heap_tree_root)
    draw_tree(heap_tree_root, "DFS Visualization")

    # BFS візуалізація
    bfs_colors = bfs_visualize(heap_tree_root)
    draw_tree(heap_tree_root, "BFS Visualization")
