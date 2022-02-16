"""
Part 2 - Chapter 08 - Q5 (page 226~)
효율적인 화폐 구성

N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.


입력 조건 :
    - 첫째 줄에 N,M이 주어진다. ( 1 <= N <= 100, 1 <= M <= 10,000)
    - 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

출력 조건 :
    - 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
    - 불가능 할 때는 -1 을 출력한다.

입력 예시1 :
2 15
2
3

출력 예시1 :
5


입력 예시2 :
3 4
3
5
7

출력 예시2 :
-1

"""


# -----------------------------------
print("\n -*-*-*-*-*- First -*-*-*-*-*- \n")

N, M = map(int, input().split())

array = []
for i in range(N):
    array.append(int(input()))

d = [10001] * (M + 1)

d[0] = 0
for i in range(N):
    for j in range(array[i], M+1):

        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1 )

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
