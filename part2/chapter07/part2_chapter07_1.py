"""
Part 2 - Chapter 07 - Q1 (page 186~)
범위를 반씩 좁혀가는 탐색
"""


def ex_7_1():
    print("\n 7-1.py 순차 탐색 소스 코드 \n")

    # 같은지 다른지 하나씩 탐색하는 함수
    def sequnential_search(n, target, array):
        for i in range(n):
            if array[i] == target:
                return i + 1  # 0부터 시작해서 1을 더해줘야함

    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()    # 5 Dongbin
    n = int(input_data[0])
    target = input_data[1]

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = input().split()     # Hanul Jonggu Dongbin Taeil Sangwook

    # 결과를 다른 곳에 저장한 후 프린트 하는 것 보다 한번에 하는게 메모리를 적게먹음
    print(sequnential_search(n, target, array))


def ex_7_2():
    print("\n 7-2.py 재귀 함수로 구현한 이진 탐색 소스 코드 \n")

    # 재귀함수로 만드는 코드
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return binary_search(array, target, mid+1, end)

    # n(원소의 개수가)과 target(찾고자 하는 문자열)을 입력받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n-1)

    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result+1)     # 몇 번째 있는지 파악하는 거기때문 (인덱스 0부터 시작)


def ex_7_3():
    print("\n 7-3.py 반복문으로 구현한 이진 탐색 소스코드 \n")

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

    # 이하 과정 동일
    # n(원소의 개수가)과 target(찾고자 하는 문자열)을 입력받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n - 1)

    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)  # 몇 번째 있는지 파악하는 거기때문 (인덱스 0부터 시작)


def ex_7_4():
    print("\n 7-4.py 한 줄 입력받아 출력하는 소스코드 \n")

    import sys
    # 하나의 문자열 데이터 입력받기
    input_data = sys.stdin.readline().rstrip()

    # 입력 받은 문자열 그대로 출력
    print(input_data)


if __name__ == '__main__':
    ex_7_1()
    ex_7_2()
    ex_7_3()
    ex_7_4()

