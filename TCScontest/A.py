import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_smallest_prime(numbers):
    q = min(numbers)
    for p in range(max(numbers), 10**10):
        if all(p % num == q for num in numbers if num != q) and is_prime(p):
            return p
            
    return "None"

# Example usage
input_numbers = list(map(int, input().split()))
result = find_smallest_prime(input_numbers)
print(result)