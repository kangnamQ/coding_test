"""
Part 2 - Chapter 07 - Q2 (page 197~)
부품 찾기

동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개 일때 부품 번호가 다음과 같다고 하자

N = 5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

M = 3
[5, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.


입력 조건 :
    - 첫째 줄에 정수 N이 주어진다. ( 1 <= N <= 1,000,000 )
    - 둘째 줄에는 공백으로 구분하여  N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하 이다.
    - 셋째 줄에 정수 M이 주어진다. ( 1 <= N <= 1,000,000 )
    - 넷째 줄에는 공백으로 구분하여  M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하 이다.

출력 조건 :
    - 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

입력 예시 :
5
8 3 7 9 2
3
5 7 9

출력 예시 :
no yes yes
"""


def ex_7_5():
    print("\n 7-5.py 이진 탐색 \n")

    # 반복문사용
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            # 찾은 경우 중간점 인덱스 반환
            if array[mid] == target:
                return mid
            # 중간점 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
            elif array[mid] > target:
                end = mid - 1
            # 찾고자 하는 값이 큰경우 오른쪽 확인
            else:
                start = mid + 1

        return None

    # N 가게 부품 개수 입력
    N = int(input())

    # 가게 부품번호 공백 구분출력
    array = list(map(int, input().split()))
    array.sort()

    # M 손님이 확인 요청한 부품 개수
    M = int(input())        # 여기서는 안쓰이넹..
    # 요청한 부품번호 공백으로 구분하여 입력
    x = list(map(int, input().split()))

    # 하나씩 확인
    for i in x:
        result = binary_search(array, i, 0, N-1)
        if result != None:
            print('yes', end=' ')  # 공백으로 구분해야하기 때문

        else:
            print('no', end=' ')


def ex_7_6():
    print("\n 7-6.py 계수 정렬 \n")
    # 다만들어서 하나씩 보는 방법...

    N = int(input())
    array = [0] * 1000001

    for i in input().split():
        array[int(i)] = 1

    M = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if array[i] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')


def ex_7_7():
    # 이게 제일 편해보이는데..
    print("\n 7-7.py 집합 자료형 이용 \n")

    N = int(input())
    array = list(map(int, input().split()))
    M = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if i in array:
            print('yes', end=' ')
        else:
            print('no', end=' ')


if __name__ == '__main__':

    ex_7_5()
    ex_7_6()
    ex_7_7()

