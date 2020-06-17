n = int(input())
assert 1 <= n <= 10 ** 5
phone_book = {}
for _ in range(n):
    name, phone_number = input().strip().split()
    phone_book[name] = phone_number
while True:
    try:
        query = input()
        print(f'{query}={phone_book[query]}' if query in phone_book else 'Not found')
    except (EOFError, BaseException) as e:
        break
