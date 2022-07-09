from heapq import nlargest
from sys import stdin


def find_rank(line):
    idx, z, p, l, c, s = map(int, line.strip().split())
    score = p * 50 + l * 5 + c * 10 + s * 20
    change = score - z
    return change, idx, score


n = int(stdin.readline())
ranking = map(find_rank, stdin.readlines())
for _, topic_id, new_score in nlargest(5, ranking):
    print(topic_id, new_score)
