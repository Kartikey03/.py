from collections import defaultdict

def splitit(N, transactions):
    accounts = defaultdict(int)

    for transaction in transactions:
        split = transaction.split('/')
        if split[1] == 'L':
            lender, borrower, amount = split[0], split[2], int(split[3][1:])
            accounts[lender] -= amount
            accounts[borrower] += amount
        else:
            payer, amount, *recipients = split
            amount = int(amount)
            num_recipients = len(recipients)
            for recipient in recipients:
                accounts[recipient] += amount // num_recipients
            accounts[payer] -= amount

    dues = []
    for person, amount in accounts.items():
        if amount != 0:
            dues.append((person, amount))

    dues.sort(key=lambda x: (x[1], x[0]))

    result = []
    for person, amount in dues:
        if amount > 0:
            break
        for _, to_pay in result:
            if to_pay + amount >= 0:
                to_pay += amount
                break
        else:
            result.append((person, amount))

    output = '\n'.join([f'{payer}/{recipient}/{abs(amount)}' for payer, recipient, amount in result])

    return output if output else "NO DUES."

def main():
    # Read input
    N = int(input())
    transactions = [input() for _ in range(N)]

    # Calculate and print the result
    result = splitit(N, transactions)
    print(result)

if __name__ == "__main__":
    main()
