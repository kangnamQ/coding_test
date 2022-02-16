"""
Part 2 - Chapter 08 - Q1 (page 208~)
다이나믹 프로그래밍
"""


def ex_8_1():
    print("\n 8-1.py 피보나치 함수 소스코드 \n")

    # 재귀 함수로 표현
    def fibo(x):
        if x == 1 or x == 2:
            return 1
        return fibo(x-1) + fibo(x-2)

    print(fibo(4))


def ex_8_2():
    print("\n 8-2.py 피보나치 수열 소스코드 (재귀) \n")

    d = [0] * 100

    # 재귀 함수로 표현
    def fibo(x):
        if x == 1 or x == 2:
            return 1

        if d[x] != 0:
            return d[x]

        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

    print(fibo(99))


def ex_8_3():
    print("\n 8-3.py 호출되는 함수 확인 \n")

    d = [0] * 100

    # 재귀 함수로 표현
    def fibo(x):
        print('f(' + str(x) + ')', end=' ')
        if x == 1 or x == 2:
            return 1

        if d[x] != 0:
            return d[x]

        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

    print(fibo(6))


def ex_8_4():
    print("\n 8-4.py 피보나치 수열 소스코드 (반복적) \n")

    d = [0] * 100

    d[1] = 1
    d[2] = 1
    n = 99

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])


if __name__ == '__main__':
    ex_8_1()
    ex_8_2()
    ex_8_3()
    ex_8_4()

