def print_logo(size):
    def is_even(x):
        return int((x % 2) == 1)

    def repeat(c, x):
        return str(c) * x

    logo = []
    for i in range(2 * size):
        if i < size:
            j = int(i / 2) + 1
            logo.append(
                repeat(" ", size - i - 1)
                + repeat(" /", j)
                + repeat("  ", is_even(i))
                + repeat("\\ ", j)
            )
        else:
            j = int(size - (i + 1) / 2) + 1
            logo.append(
                repeat(" ", i - size + 2)
                + repeat(" \\", j)
                + repeat("  ", is_even(i + 1))
                + repeat("/ ", j)
            )
    for row in logo:
        print(row[1:].rstrip())


n = int(input())
print_logo(n)
print_logo(n + 1)
