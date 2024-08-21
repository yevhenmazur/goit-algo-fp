import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    '''Реалізація алгоритму Дейкстри'''
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


# Задаю граф
G = nx.Graph()
edges = [
    ('A', 'B', 7),
    ('A', 'C', 9),
    ('A', 'F', 14),
    ('B', 'C', 10),
    ('B', 'D', 15),
    ('C', 'D', 11),
    ('C', 'F', 2),
    ('D', 'E', 6),
    ('E', 'F', 9),
    ('E', 'G', 8),
    ('F', 'G', 12),
    ('G', 'H', 7),
    ('H', 'I', 5),
    ('H', 'J', 4),
    ('I', 'J', 6),
    ('J', 'K', 3),
    ('K', 'L', 4),
    ('L', 'F', 5),
]
G.add_weighted_edges_from(edges)

# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "A")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G, k=2)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
