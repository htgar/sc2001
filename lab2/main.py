import random
import time
import heapq
import csv


def generate_graph_adj_matrix(n, edge_prob=0.3, seed=42):
    random.seed(seed)
    matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                w = random.randint(1, 100)
                matrix[i][j] = w
                matrix[j][i] = w
    return matrix


def generate_graph_adj_list(n, edge_prob=0.3, seed=42):
    random.seed(seed)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                w = random.randint(1, 100)
                adj[i].append((j, w))
                adj[j].append((i, w))
    return adj


def dijkstra_array(matrix, start):
    n = len(matrix)
    dist = [float("inf")] * n
    visited = [False] * n
    dist[start] = 0

    for i in range(n):
        u = -1
        min_dist = float("inf")
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if not visited[v] and matrix[u][v] < float("inf"):
                nd = dist[u] + matrix[u][v]
                if nd < dist[v]:
                    dist[v] = nd
    return dist


def dijkstra_heap(adj, start):
    n = len(adj)
    dist = [float("inf")] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def count_edges(adj):
    return sum(len(v) for v in adj) // 2


if __name__ == "__main__":
    sizes = [10, 50, 100, 200, 500, 1000]
    edge_prob = 0.3

    results = []
    print(f"{'V':>5} {'E':>8} {'Array (s)':>12} {'Heap (s)':>12}")
    print("-" * 40)

    for n in sizes:
        matrix = generate_graph_adj_matrix(n, edge_prob, seed=n)
        adj = generate_graph_adj_list(n, edge_prob, seed=n)
        e = count_edges(adj)

        iters = 100 if n <= 100 else 20 if n <= 500 else 5

        t0 = time.time()
        for i in range(iters):
            dijkstra_array(matrix, 0)
        t_array = (time.time() - t0) / iters

        t0 = time.time()
        for i in range(iters):
            dijkstra_heap(adj, 0)
        t_heap = (time.time() - t0) / iters

        results.append((n, e, t_array, t_heap))
        print(f"{n:>5} {e:>8} {t_array:>12.6f} {t_heap:>12.6f}")

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["V", "E", "Array_Time", "Heap_Time"])
        writer.writerows(results)

    print("\n(a) Adjacency Matrix + Array PQ: O(V^2)")
    print("(b) Adjacency List + Min-Heap: O((V+E) log V)")
    print("\nResults saved to results.csv")
