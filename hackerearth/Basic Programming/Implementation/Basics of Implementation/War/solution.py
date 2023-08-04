t = int(input())
for _ in range(t):
    n = int(input())
    bob_army = list(map(int, input().strip().split()))
    alice_army = list(map(int, input().strip().split()))
    bob_strongest = max(bob_army)
    alice_strongest = max(alice_army)
    if bob_strongest > alice_strongest:
        print('Bob')
    elif bob_strongest < alice_strongest:
        print('Alice')
    else:
        print('Tie')
