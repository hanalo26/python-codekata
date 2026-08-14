# k진수에서 소수 개수 구하기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92335
# 알고리즘: 수학, 문자열
# 작성자: 백하은
# 작성일: 2026. 08. 14. 16:33:24

import math

# 1. n을 k진법 문자열로 변환하는 함수
def to_k_nums(n,k):
    res = ""
    
    while n > 0:
        res = str(n % k) + res
        n = n // k
    return res

# 2. 소수 판정 함수 (O(sqrt(x)))
def is_prime(a):
    if a < 2:
        return False

    for i in range(2, int(math.isqrt(a))+1):
        if a % i == 0:
            return False
        
    return True

# 3. 메인
def solution(n, k):
    answer = 0
    
    # n을 k진수로 변환
    k_num_str = to_k_nums(n,k)
    
    # '0'을 기준으로 숫자를 분할
    candidates = k_num_str.split('0') # 자돟으로 리스트에 담김
    
    for c in candidates:
        # 빈 문자열('')이 아니고, 소수인 경우 카운트
        if c and is_prime(int(c)):
            answer += 1
            
    return answer