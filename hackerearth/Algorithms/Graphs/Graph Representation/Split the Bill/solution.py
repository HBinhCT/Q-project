n, m = map(int, input().strip().split())
balances = [0] * n
for _ in range(m):
    transaction_id = input().strip()
    n_payers, n_splits = map(int, input().strip().split())
    for _ in range(n_payers):
        payer, amount = map(int, input().strip().split())
        balances[payer - 1] -= amount
    for _ in range(n_splits):
        borrower, amount = map(int, input().strip().split())
        balances[borrower - 1] += amount
payments = []
j = 0
for i in range(n):
    if balances[i] > 0:
        current_balance = balances[i]
        while current_balance > 0 and j < n:
            if balances[j] >= 0:
                j += 1
                continue
            min_balance = min(current_balance, abs(balances[j]))
            current_balance -= min_balance
            balances[j] += min_balance
            payments.append((i + 1, j + 1, min_balance))
for payment in payments:
    print(*payment)
