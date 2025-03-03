from collections import defaultdict, deque

def pick_up_service(N, routes):
    graph = defaultdict(list)
    goods = {}
    tax = {}

    for _ in range(N-1):
        city1, city2, num_goods, entry_tax = routes[_]
        graph[city1].append(city2)
        graph[city2].append(city1)
        goods[city2] = num_goods
        tax[city2] = entry_tax

    visited = set()
    route = []

    def dfs(city):
        nonlocal route
        visited.add(city)
        neighbors = graph[city]
        neighbors.sort(key=lambda x: (-goods[x], tax[x], x))

        for neighbor in neighbors:
            if neighbor not in visited:
                route.append((city, neighbor))
                dfs(neighbor)

    dfs("hyderabad")

    total_tax = 0
    for edge in route:
        total_tax += tax[edge[1]]

    route_str = '-'.join([city[0] for city in route[-1::-1][:-1] + route])

    return route_str, total_tax

def main():
    # Read input
    N = int(input())
    routes = [input().split() for _ in range(N - 1)]

    # Calculate and print the result
    result, total_tax = pick_up_service(N, routes)
    print(result)
    print(total_tax)

if __name__ == "__main__":
    main()
