
def minimumSum(self, k: int, n: int) -> int:
    if k == 1:
        # If k is 1, the array can be [1, 2, 3, ..., n]
        return n * (n + 1) // 2

    # Initialize the result to store the sum of the k-avoiding array
    result = 0

    # Start with the smallest possible element: 1
    num = 1

    # Iterate n times to generate the k-avoiding array
    for i in range(n):
        result += num
        num = num + k - 1

    return result
minimumSum(1,5,4)