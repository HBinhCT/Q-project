#!/bin/python3


def most_commons(logo):
    from collections import Counter
    count = Counter(logo)
    return [f'{k} {v}' for v in sorted(set(count.values()), reverse=True) for k in
            sorted(k for k in count if count[k] == v)][:3]


if __name__ == '__main__':
    s = input()
    assert 3 < len(s) <= 10 ** 4
    result = most_commons(s)
    print(*result, sep='\n')
