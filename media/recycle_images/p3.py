import math
from collections import defaultdict, deque

def connect(adjclist, device1, device2, distance, angle):
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    adjclist[device1].append((device2, x, y))
    adjclist[device2].append((device1, -x, -y))  

def finddist(adjclist, start, target):
    q = deque([(start, 0.0, 0.0)])
    vis = set([start])
    
    while q:
        curr, sumxval, sumyval = q.popleft()
        if curr == target: return math.sqrt(sumxval ** 2 + sumyval ** 2)
        
        for adj, dx, dy in adjclist[curr]:
            if adj not in vis:
                vis.add(adj)
                q.append((adj, sumxval + dx, sumyval + dy))
    return -1  

n = int(input().strip())
devices = input().strip().split()
adjclist = defaultdict(list)

for _ in range(n):
    devid = int(input().strip())
    conn = int(devices[devid - 1].split(':')[1])
    for _ in range(conn):
        nid, dist, angle = map(int, input().strip().split())
        connect(adjclist, devid, nid, dist, angle)
start, end = map(int, input().strip().split())

distance = finddist(adjclist, start, end)
if distance != -1: print(f"{distance:.2f}")
else: print("Path not found")
