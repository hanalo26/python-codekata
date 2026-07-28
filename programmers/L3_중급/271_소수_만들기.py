# 소수 만들기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 알고리즘: 완전탐색, 수학
# 작성자: 백하은
# 작성일: 2026. 07. 28. 19:09:45

from itertools import combinations

# prime number 여부 판정 함수
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

# 3가지 숫자를 골라 더한 합이 소수인 경우의 수를 계산하는 함수
def solution(nums):
    answer = 0
    
    for combo in combinations(nums,3):
        total = sum(combo)
        
        if is_prime(total):
            answer += 1

    return answer