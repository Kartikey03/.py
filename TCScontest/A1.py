def simplify_to_single_digit(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

def generate_password(number, name):
    try:
        num_parts = number.split('.')
        if len(num_parts) == 1:
            num_parts.append('0')  # Handle integers by adding a decimal part
        num_parts[0] = simplify_to_single_digit(int(num_parts[0]))
        num_parts[1] = simplify_to_single_digit(int(num_parts[1]))

        scientific_notation = f"{num_parts[0]}.{num_parts[1]}e{num_parts[1]}"
        s1 = ''.join([word[:3] for word in map(str, scientific_notation) if word.isnumeric() or word == 'e'])
        s2 = ''.join([name[i] for i in range(len(name)) if (i + 1) % 2 == num_parts[1] % 2])

        password = f"{s1}@{s2}"
        return password
    except ValueError:
        return "Invalid input"

def main():
    t = int(input())
    for _ in range(t):
        data = input().split()
        number, name = data[0], data[1]
        password = generate_password(number, name)
        print(password)

if __name__ == "__main__":
    main()
