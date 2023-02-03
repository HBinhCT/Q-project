from collections import defaultdict


def search(start, end, adjacency, seen, path, res, total=0):
    seen[start] = True
    path.append(start)
    if start == end:
        res.append((total, len(path), ' '.join(path)))
    else:
        if start in adjacency:
            for connecting, amount in adjacency[start]:
                if not seen[connecting]:
                    search(connecting, end, adjacency, seen, path, res, total + amount)
    path.pop()
    seen[start] = False


departure, arrival = input().strip().split()
flights = defaultdict(list)
visited = {}
while True:
    try:
        departure_name, arrival_name, cost = input().strip().split()
        flights[departure_name].append((arrival_name, int(cost)))
        visited[departure_name] = False
        visited[arrival_name] = False
    except:
        break
ans = []
options = []
search(departure, arrival, flights, visited, options, ans)
ans.sort()
if not ans:
    print('No Flights')
else:
    for total_cost, count, route in ans:
        print(route, total_cost)
