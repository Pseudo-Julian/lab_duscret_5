def greedy_coloring(graph):
    colors = {}  # словник, де ключ - вершина, значення - колір

    # Перебираємо вершини графа
    for node in graph:
        used_colors = set()  # використані кольори для поточної вершини

        # Перебираємо сусідів поточної вершини
        for neighbor in graph[node]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        # Знаходимо найменший доступний колір
        color = 1
        while color in used_colors:
            color += 1

        colors[node] = color  # присвоюємо вершині знайдений колір

    return colors

def main():
    # Введення матриці суміжності
    n = int(input("Введіть кількість вершин графа: "))
    print("Введіть матрицю суміжності (1 - є ребро, 0 - немає ребра):")

    graph = {}
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        graph[i] = [j for j, value in enumerate(row, start=1) if value == 1]

    # Виклик жадібного алгоритму
    coloring_result = greedy_coloring(graph)

    # Виведення результату
    print("\nРезультат розфарбування:")
    for node, color in coloring_result.items():
        print(f"Вершина {node}: Колір {color}")

if __name__ == "__main__":
    main()
