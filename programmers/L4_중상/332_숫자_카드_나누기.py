# 숫자 카드 나누기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 알고리즘: 수학, GCD
# 작성자: 백하은
# 작성일: 2026. 11. 06. 13:48:32

"""
(1) 구해야 하는 것: 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a
    - 단 두 조건을 모두 만족하지 않는 경우에는 0을 반환할 것
    
(2) 양의 정수를 선택하는 조건
    - a가 철수가 가진 모든 숫자 카드의 숫자를 나눌 수 있어야 하지만, 영희가 가진 모든 숫자 카드의 숫자를 전부 나눌 수는 없어야 함
    - a가 영희가 가진 모든 숫자 카드의 숫자를 나눌 수 있어야 하지만, 철수가진 모든 숫자 카드의 숫자를 전부 나눌 수는 없어야 함
    -> a는 영희 또는 철수가 가진 모든 숫자 카드의 숫자들 간의 최대 공약수가 되어야 함
    
(3) arrayA : 철수의 숫자 카드
(4) arrayB : 영희의 숫자 카드 
"""
import math

# 최대공약수를 구하는 함수
def find_gcd(arr):
    # 최대공약수의 첫번째 후보로 첫번째 원소 지정(추후에 반복문을 거치면서 최대공약수가 계속 저장될 예정)
    g = arr[0]
    for x in arr[1:]:
        # 최대공약수를 구하는 매서드
        g = math.gcd(g,x)
        
    return g

# 문제의 조건을 만족하는 가장 큰 양의 정수 a를 구하는 함수
def solution(arrayA, arrayB):
    # 철수와 영희 카드들의 전체 최대공약수 구하기
    gcd_A = find_gcd(arrayA)
    gcd_B = find_gcd(arrayB)
    
    answer = 0
    
    # 후보 1 (gcd_A) 검증: 철수 카드는 다 나누고, 영희 카드는 하나도 못 나눠야 함
    possible_A = True
    
    for x in arrayB:
        if x % gcd_A == 0:
            possible_A = False
            
    if possible_A:
        answer = max(answer, gcd_A)
    
    # 후보 2 (gcd_B) 검증: 영희 카드는 다 나누고, 철수 카드는 하나도 못 나눠야 함
    possible_B = True
    
    for x in arrayA:
        if x % gcd_B == 0:
            possible_B = False
            
    if possible_B:
        answer = max(answer, gcd_B)
    
    return answer