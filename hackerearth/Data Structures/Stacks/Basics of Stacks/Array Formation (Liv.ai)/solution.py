def queue_and_stack(A):
    # Write your code here
    ln = max(A)
    primes = [True] * (ln + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i < ln:
        if primes[i]:
            for j in range(i * 2, ln + 1, i):
                primes[j] = False
        i += 1
    stack = []
    queue = []
    for i in A:
        if primes[i]:
            queue.append(i)
        else:
            stack.append(i)
    return [queue, reversed(stack)]


n = int(input())
A = list(map(int, input().strip().split()))

out_ = queue_and_stack(A)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
