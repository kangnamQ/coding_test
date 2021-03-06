"""
Part 2 - Chapter 04 - Q2 (page 113)
시각

정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
- 00시 00분 03초
- 00시 13분 30초

반명에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
- 00시 02분 55초
- 01시 27분 45초

입력 조건 :
    - 첫째 줄에 정수 N이 입력된다. (1 <= N <= 23)

출력 조건 :
    - 00시 00분 00초부터  N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

입력 예시 :
    5

출력 예시 :
    11475

"""
# First : 직접 코딩
# Second ~ : 답안 예시 및 해설의 도움
# -----------------------------------
print("\n -*-*-*-*-*- First -*-*-*-*-*- \n")

N = int(input())
count = 0

for hour in range(N+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(min) + str(sec):
                count += 1

print(count)


# -------------------------------------------
# print("\n -*-*-*-*-*- Second -*-*-*-*-*- \n")
# 큰 차이 없어서 생략


