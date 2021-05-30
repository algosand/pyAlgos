
from collections import defaultdict


def simulate(x, A, B, limit):
    cnt = 20
    nxt = [x]
    seen = defaultdict(int)
    seen[x] += 1
    while cnt > 0 and len(nxt) > 0:
        n = nxt.pop()
        u = n-A
        v = n-B
        if u > limit:
            nxt.append(u)
            seen[u] += 1
        if v > limit:
            nxt.append(v)
            seen[v] += 1
        if u == limit:
            seen[u] += 1
            cnt -= 1
        if v == limit:
            cnt -= 1
            seen[v] += 1
    print(cnt)
    print(seen)


if __name__ == '__main__':
    simulate(300, 19, 20, 20)
    simulate(400, 19, 20, 20)
    simulate(402, 19, 20, 20)
