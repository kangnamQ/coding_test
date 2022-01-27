"""
Part 2 - Chapter 06 - Q1 (page 156~)
기준에 따라 데이터를 정렬
"""


def ex_6_1():
    print("\n 6-1.py 선택 정렬 소스 코드 \n")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i
        for j in range(i +1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array [min_index], array[i]

    print(array)


def ex_6_2():
    print("\n 6-2.py 파이썬 스와프 소스코드 \n")
    array = [3, 5]
    array[0], array[1] = array[1], array[0]

    print(array)


def ex_6_3():
    print("6-3.py 삽입 정렬 소스코드")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # i부터 0까지 -1씩 이동하며 반복한다고 함
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    print(array)


def ex_6_4():
    print("6-4.py 퀵 정렬 소스코드")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array, start, end):
        if start >= end:
            return

        pivot = start
        left = start + 1
        right = end
        while left <= right:
            # 피벗보다 큰 데이터를 찾을 때까지 반복
            while left <= end and array[left] <= array[pivot]:
                left += 1
            # 피벗보다 작은 데이터를 찾을 때까지 반복
            while right > start and array[right] >= array[pivot]:
                right -= 1
            # 엇갈릴 경우 작은 데이터와 피벗 교체
            if left > right:
                array[right], array[pivot] = array[pivot], array[right]
            # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
            else:
                array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분 정렬
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end )

    quick_sort(array, 0, len(array)-1)
    print(array)


def ex_6_5():
    print("6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array):
        if len(array) <= 1:
            return array

        pivot = array[0]    # 피벗은 처음 원소
        tail = array[1:]    # 나머지 리스트

        left_side = [x for x in tail if x <= pivot]     # 왼쪽 부분 (pivot보다 작은 부분)
        right_side = [x for x in tail if x > pivot]     # 오른쪽 부분 (pivot보다 큰 부분)

        # pivot을 기준으로 양쪽의 데이터 정렬
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    print(quick_sort(array))


def ex_6_6():
    print("6-6.py 계수 정렬 소스 코드")
    # 모든 원소의 값이 0보다 크거나 같다고 가정
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    # 모든 범위를 포함하는 리스트 선언(0으로 초기화)
    count = [0] * (max(array)+1)

    # 각 데이터에 해당하는 인덱스 값 증가
    for i in range(len(array)):
        count[array[i]] += 1

    # 리스트에 기록된 정렬 정보 확인 및 띄어쓰기 구분으로 등장 횟수만큼 인덱스 출력
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


def ex_6_7():
    print("6-7.py sorted 소스코드")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    result = sorted(array)
    print(result)


def ex_6_8():
    print("6-8.py sort 소스코드")
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    array.sort()
    print(array)


def ex_6_9():
    print("6-9.py 정렬 라이브러리에서 key를 활용한 소스코드")
    array = [('바나나', 2), ('사과', 5), ('당근', 3)]

    def setting(data):
        return data[1]

    # key에 함수도 넣을 수 있네..
    result = sorted(array, key=setting)
    print(result)


if __name__ == '__main__':
    ex_6_1()
    ex_6_2()
    ex_6_3()
    ex_6_4()
    ex_6_5()
    ex_6_6()
    ex_6_7()
    ex_6_8()
    ex_6_9()
