import sys
from itertools import permutations

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def min_distance_traveled(passengers, vehicles):
    min_distance = sys.maxsize
    vehicle_permutations = permutations(vehicles)

    for perm in vehicle_permutations:
        distance = 0
        passengers_copy = list(passengers)

        for vehicle in perm:
            passenger = min(passengers_copy, key=lambda x: (manhattan_distance(x[1:], vehicle[1:]), x[0]))
            distance += manhattan_distance(passenger[1:], vehicle[1:])
            passengers_copy.remove(passenger)

        min_distance = min(min_distance, distance)

    return min_distance

def main():
    # Read input
    N, M = map(int, input().split())
    passengers = [input().split() for _ in range(N)]
    vehicles = [input().split() for _ in range(M)]

    # Calculate and print the result
    result = min_distance_traveled(passengers, vehicles)
    print(result)

if __name__ == "__main__":
    main()
