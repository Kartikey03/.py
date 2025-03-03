def min_vehicles(arr, k):
    arr.sort(reverse=True)
    vehicles = 0
    i = 0

    while i < len(arr):
        current_weight = arr[i]
        i += 1

        while i < len(arr) and current_weight + arr[i] <= k:
            current_weight += arr[i]
            i += 1

        vehicles += 1

    return vehicles

def main():
    # Read input
    weights = list(map(int, input().split()))
    k = int(input())

    # Calculate and print the result
    result = min_vehicles(weights, k)
    print(result)

if __name__ == "__main__":
    main()
