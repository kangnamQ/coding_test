"""
Part 2 - Chapter 03 - Q1 (page 87)
거스름 돈

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""
# -----------------------------------
print("\n -*-*-*-*-*- First -*-*-*-*-*- \n")

N = 1780
change_coin = 0
coin_type = [500, 100, 50, 10]

for loop in range(len(coin_type)):
    print("Coin_type : ", coin_type[loop])
    change_count =  (N // coin_type[loop])
    change_coin = change_coin + change_count
    N = N % coin_type[loop]
    print("Coin Count : ", change_count)
    print("N : ", N)
    # // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    # % : 나누기 연산 후 몫이 아닌 나머지를 구함
print("change coin : ", change_coin)



# -------------------------------------------
print("\n -*-*-*-*-*- Second -*-*-*-*-*- \n")

N = 1780
change_coin = 0
coin_type = [500, 100, 50, 10]

for loop in coin_type:
    # 1. 리스트 구조에서 for문을 돌때 굳이 range로 안잡아도 list의 순서대로 값이 나옴 (코드가 더 간결해짐)
    print("Coin_type : ", loop)
    change_coin += N // loop
    # 2. 굳이 새로운 변수를 안만들고 직접 +=나 %=를 사용해서 계산 (메모리 효율이 더 좋음, 코드도 더 간결)
    N %= loop
    print("Coin Count : ", change_coin)
    print("N : ", N)
print("change coin : ", change_coin)


# -------------------------------------------
print("\n -*-*-*-*-*- Final -*-*-*-*-*- \n")

N = 1780
change_coin = 0
coin_type = [500, 100, 50, 10]

for loop in coin_type:
    change_coin += N // loop
    N %= loop
print("change coin : ", change_coin)
