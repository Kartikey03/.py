import math
import time

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes

def find_smallest_prime(numbers):
    q = min(numbers)
    max_number = max(numbers)

    primes = sieve_of_eratosthenes(max_number + 1)  # Increase the size of the primes list
    for p in range(max_number, 10**10):
        if all(p % num == q for num in numbers if num != q) and primes[p]:
            return p
    return "None"

# Example usage
input_numbers = [3, 4, 5, 1]
start_time = time.time()
result = find_smallest_prime(input_numbers)
end_time = time.time()
execution_time = end_time - start_time

print(result)