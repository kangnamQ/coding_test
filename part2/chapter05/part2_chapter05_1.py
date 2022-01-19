"""
Part 2 - Chapter 05 - Q1 (page 124~)
꼭 필요한 자료구조 기초
"""


def ex_5_1_1():
    print("\n 5-1.py stack example \n")
    print("삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()")
    # 선입 후출 또는 후입 선출 구조
    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    print(stack)
    print(stack[::-1])

    """
    :: 사용법
    arr[::2]  # 처음부터 끝까지 두 칸 간격으로
    arr[1::2]  # index 1부터 끝까지 두 칸 간격으로
    arr[::-1]  # 처음부터 끝까지 -1칸 간격으로 (역순으로)
    arr[3::-2]  # index 3부터 끝까지 -2칸 간격으로 
    arr[1:6:2]  # index 1부터 6까지 두칸 간격으로
    """


def ex_5_1_2():
    print("\n 5-2.py queue example \n")
    print("삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()")
    # 선입 선출 구조
    from collections import deque
    # deque라이브러리 사용한다고 함

    queue = deque()
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue)    # 먼저 들어온게 나옴
    queue.reverse()  # 순서 반전
    print(queue)    # 반전됬으므로 마지막에 들어온것 부터 나옴


def ex_5_1_3():
    print("5-3.py recursive function(재귀 함수) example")
    ex_5_1_3()

    # 무한으로 출력하다가 어느순간 재귀의 최대 깊으를 초과했다는 에러메시지가 나옴.
    # 기본적으로 파이썬 인터프리터엔 호출 횟수 제한이 있음


def ex_5_1_4(i=0):
    print("5-4.py recursive function(재귀 함수) 종료 example")
    if i == 100:
        return
    print(f"{i}번째 재귀 함수에서 {i+1}번째 재귀 함수를 호출합니다.")
    ex_5_1_4(i + 1)
    print(f"{i}번째 재귀 함수를 종료합니다.")


def ex_5_1_5(n=1):
    print("5-5.py factorial example")

    def factorial_iterative(n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def factorial_recursive(n):
        if n <= 1:
            return 1
        return n * factorial_recursive(n - 1)

    print("반복적으로 구현 : ", factorial_iterative(5))
    print("재귀적으로 구현 : ", factorial_recursive(5))

    print("두 가지 경우 모두 120이 나와야 정상")


if __name__ == '__main__':
    ex_5_1_1()
    ex_5_1_2()
    # ex_5_1_3() << 에러나오게 코딩한거라 에러나옴
    ex_5_1_4(i=1)
    ex_5_1_5(n=1)
