"""
Part 2 - Chapter 09 - Q1 (page 230~)
가장 빠른 길 찾기
"""


def ex_9_1():
    print("\n 9-1.py 간단한 다익스트라 알고리즘 소스코드 \n")
    import sys

    input = sys.stdin.readline
    # 10억 값으로 무한을 설정
    INF = int(1e9)

    N,M = map(int, input().split())
    start = int(input())

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담든 리스트
    graph = [[] for i in range(N+1)]
    # 방문한 적이 있는지 체크하는 리스트
    visited = [False] * (N+1)
    # 최단거리 테이블 무한 초기화
    distance = [INF] * (N+1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b, c))

    # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value = INF
        index = 0 # 가장 최단 거리가 짧은 노드

        for i in range(1, N+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i

        return index

    def dijkstra(start):
        # 시작노드 초기화
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

            # 시작노드를 제외하기 때문에 n-1
            for i in range(N-1):
                # 최단 거리 노드를 꺼내 방문처리
                now = get_smallest_node()
                visited[now] = True

                for j in graph[now]:
                    cost = distance[now] + j[1]
                    # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                    if cost < distance[j[0]]:
                        distance[j[0]] = cost

    dijkstra(start)

    for i in range(1, N+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


def ex_9_2():
    print("\n 9-2.py 개선된 다익스트라 알고리즘 소스코드 \n")
    import heapq
    import sys
    input = sys.stdin.readline
    # 10억 값으로 무한을 설정
    INF = int(1e9)

    N, M = map(int, input().split())
    start = int(input())

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담든 리스트
    graph = [[] for i in range(N + 1)]
    # 방문한 적이 있는지 체크하는 리스트
    visited = [False] * (N + 1)
    # 최단거리 테이블 무한 초기화
    distance = [INF] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b, c))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        # q가 비어있지 않다면
        while q:
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들 확인
            for i in graph[now]:
                cost = dist + i[1]
                #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start)

    for i in range(1, N+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


def ex_9_3():
    print("\n 9-3.py 플로이드 워셜 알고리즘 소스코드 \n")

    INF = int(1e9)

    N = int(input())
    M = int(input())

    # 2차원 리스트(그래프 표현)을 만들고 모든 값을 무한으로 초기화
    graph = [[INF] * (N+1) for _ in range(N+1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for _ in range(M):
        # A 에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 결과물 출력
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()


if __name__ == '__main__':
    ex_9_1()
    ex_9_2()
    ex_9_3()

