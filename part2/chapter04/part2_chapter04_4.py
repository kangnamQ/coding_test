"""
Part 2 - Chapter 04 - Q4 (page 118)
게임 개발

현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼은 이러하다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진한다. 왼쪽에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아온다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

입력 조건 :
    - 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
    - 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
        방향 d의 값으로는 다음과 같이 4가지가 존재한다.
        - 0 : 북쪽
        - 1 : 동쪽
        - 2 : 남쪽
        - 3 : 서쪽
    - 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
    앱의 외각은 항상 바다로 되어 있다.
        - 0 : 육지
        - 1 : 바다
    - 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

출력 조건 :
    - 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

입력 예시 :
    4 4         # 4 * 4 맵 생성
    1 1 0       # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
    1 1 1 1     # 첫 줄은 모두 바다
    1 0 0 1     # 둘째 줄은 바다/육지/육지/바다
    1 1 0 1     # 셋째 줄은 바다/바다/육지/바다
    1 1 1 1     # 넷째 줄은 모두 바다

출력 예시 :
    3

"""
# First : 직접 코딩
# Second ~ : 답안 예시 및 해설의 도움
# -----------------------------------
print("\n -*-*-*-*-*- First -*-*-*-*-*- \n")

N, M = map(int, input().split())
visit = [0] * N
for row in range(N):
    visit[row] = [0] * M

x, y, d = map(int, input().split())
visit[x][y] = 1

point = []
for i in range(N):
    point.append(list(map(int, input().split())))

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

count = 1  # 첫 시작지점부터 1을 주었기 때문
turn = 0

while True:
    d -= 1
    if d == -1:
        d = 3

    nx = x + moves[d][0]
    ny = y + moves[d][1]
    if visit[nx][ny] == 0 and point[nx][ny] == 0:  # 방문안함 and 육지
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx = x - moves[d][0]
        ny = y - moves[d][1]

        if point[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break

        turn = 0

print(count)

# -------------------------------------------
print("\n -*-*-*-*-*- Second -*-*-*-*-*- \n")

N, M = map(int, input().split())
d = [[0] * M for _ in range(N)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1  # 첫 시작지점부터 1을 주었기 때문
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 방문안함 and 육지
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)


