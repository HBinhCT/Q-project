def repetitive_k_sums(k, arr):
    from collections import defaultdict
    from itertools import combinations_with_replacement

    values = [arr[0] // k]
    combinations = defaultdict(int)
    for i in arr[1:]:
        if combinations[i] > 0:
            combinations[i] -= 1
        else:
            combinations[i] -= 1
            new_val = i - (values[0] * (k - 1))
            for j in range(k):
                for new_comb in map(lambda x: (k - j) * new_val + sum(x), combinations_with_replacement(values, j)):
                    combinations[new_comb] += 1
            values.append(new_val)
    return values


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        s = list(map(int, input().strip().split()))
        result = repetitive_k_sums(k, s)
        print(*result)
