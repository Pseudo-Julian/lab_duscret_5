import networkx as nx
import matplotlib.pyplot as plt


def greedy_coloring(graph):
    colors = {}

    for node in graph:
        used_colors = set()

        for neighbor in graph[node]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        color = 1
        while color in used_colors:
            color += 1

        colors[node] = color

    return colors


def draw_colored_graph(graph, colors):
    G = nx.Graph()

    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  # Позиції вершин для відображення

    node_colors = [colors[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_color='white')

    # Вивід кольорів вершин
    for node, color in colors.items():
        x, y = pos[node]
        plt.text(x, y, str(color), fontsize=12, color='black', ha='center', va='center')

    plt.show()


def main():
    n = int(input("Введіть кількість вершин графа: "))
    print("Введіть матрицю суміжності (1 - є ребро, 0 - немає ребра):")

    graph = {}
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        graph[i] = [j for j, value in enumerate(row, start=1) if value == 1]

    coloring_result = greedy_coloring(graph)

    print("\nРезультат розфарбування:")
    for node, color in coloring_result.items():
        print(f"Вершина {node}: Колір {color}")

    draw_colored_graph(graph, coloring_result)


if __name__ == "__main__":
    main()



'''
0 1 1 1 1 1
1 0 1 0 0 1
1 1 0 0 0 1
1 0 0 0 1 1 
1 0 0 1 0 1
1 1 1 1 1 0
'''