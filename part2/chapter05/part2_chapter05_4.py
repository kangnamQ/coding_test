"""
Part 2 - Chapter 05 - Q4 (page 152)
미로 탈출

동빈이는 N * M 크리긔 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 있는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸은 모두 포함해서 계산한다.


입력 조건 :
    - 첫째 줄에 두 정수 N, M ( 4 <= N, M <= 200 )이 주어집니다.
      다음 N개의 줄에는 각각 M개의 정수 ( 0 혹은 1 )로 미로의 정보가 주어진다.
      각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
      또한 시작 칸과 마지막 칸은 항상 1이다.

출력 조건 :
    - 첫째 줄에 최소 이동 칸의 개수를 출력한다.

입력 예시 :
5 6
101010
111111
000001
111111
111111

출력 예시 :
    10

"""
"""
++ BFS를 이용하면 간단히 해결할 수 있다
1. 맨 처음에 (1, 1)의 위치에서 시작하며, (1, 1)의 값은 항상 1이라고 문제에서 언급되어 있다.
2. (1, 1)좌표에서 상, 하, 좌, 우로 탐색을 진행하면 바로 옆 노드인 (1, 2)위치의 노드를 방문하게 되고 새롭게 방문하는 (1, 2)노드의 값을 2로 바꾸게 된다.
3. 마찬가지로 BFS를 계속 수행하면 결과적으로 최단 경로의 값들이 1씩 증가하는 형태로 변경 된다.
"""

# -----------------------------------
print("\n -*-*-*-*-*- First -*-*-*-*-*- \n")
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


# move = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #  가능
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            #     nx = x + move[i][0]  # 가능
            #     ny = y + move[i][1]  # 가능
            nx = x + dx[i]
            ny = y + dy[i]

            # 제약 공간을 벋어날 경우 무시
            if N <= nx or nx < 0 or M <= ny or ny < 0:
                continue

            # 괴물이 있는 부분은 무시
            if graph[nx][ny] == 0:
                continue

            # 괴물이 없는 안전한 부분만 사용
            # 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print(queue)

    return graph[N-1][M-1]
    # 가장 오른쪽 아래의 최단 거리 반한
    # 도착이 (N, M)지점이니


print(bfs(0, 0))
