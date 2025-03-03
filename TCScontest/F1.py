from itertools import combinations

def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def can_win_game(N, coordinates, m):
    coordinates.sort(key=lambda x: (x[1], x[0]))

    for combination in combinations(coordinates, m):
        valid = True
        for nail in combination:
            remaining_nails = [n for n in coordinates if n not in combination]
            remaining_area = calculate_area(*remaining_nails[0], *remaining_nails[1], *remaining_nails[2])
            new_area = calculate_area(*remaining_nails[0], *remaining_nails[1], nail[0], nail[1])
            if new_area >= remaining_area:
                valid = False
                break

        if valid:
            return combination, "YES"

    return None, "NO"

def main():
    # Read input
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    m = int(input())

    # Calculate and print the result
    result, can_win = can_win_game(N, coordinates, m)
    if result:
        for nail in result:
            print(*nail)
    print(can_win)

if __name__ == "__main__":
    main()

