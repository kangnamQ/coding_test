"""
Part 2 - Chapter 05 - Q2 (page 134~)
탐색 알고리즘 DFS/BFS

DFS : Depth - First Search
깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

BFS : Breadth First Search
너비 우선 탐색이라고 부르며 가까운 노드부터 탐색하는 알고리즘이다.
"""


def ex_5_2_1():
    print("\n 5-6.py 인접 행렬 방식 example \n")

    INF = 999999999

    graph = [[0, 7, 5],
             [7, 0, INF],
             [5, INF, 0]]

    print(graph)


def ex_5_2_2():
    print("\n 5-7.py 인접 리스트 방식 example \n")

    graph = [[] for _ in range(3)]  # 3행인 2차원 리스트
    #  (노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))
    graph[1].append((0, 7))
    graph[2].append((0, 5))

    print(graph)


def ex_5_2_3():
    print("\n 5-8.py DFS 예제 example \n")

    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')

        # 현재 노드와 연결된 다른 노드를 재귀적으로 반복
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i ,visited)

    graph = [[],
             [2, 3, 8],
             [1, 7],
             [1, 4, 5],
             [3, 5],
             [3, 4],
             [7],
             [2, 6, 8],
             [1, 7]]

    visited = [False] * 9

    dfs(graph, 1, visited)


def ex_5_2_4():
    print("\n 5-9.py BFS example \n")
    from collections import deque
    # 큐 할때 사용했던 라이브러리

    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:    # queue가 빌 때까지 반복 됨
            v = queue.popleft()
            print(v, end=' ')
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    graph = [[],
             [2, 3, 8],
             [1, 7],
             [1, 4, 5],
             [3, 5],
             [3, 4],
             [7],
             [2, 6, 8],
             [1, 7]]

    visited = [False] * 9

    bfs(graph, 1, visited)


if __name__ == '__main__':
    ex_5_2_1()
    ex_5_2_2()
    ex_5_2_3()
    ex_5_2_4()
