t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    print(
        " + ".join(
            reversed(
                [f"({n}<<{i})" for i, v in enumerate(bin(m)[2:][::-1]) if v == "1"]
            )
        )
    )
