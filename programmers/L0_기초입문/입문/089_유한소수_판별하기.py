# 유한소수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120878
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 22. 13:53:23

import math

def solution(a, b):
    # math.gcd(a,b) - a,b의 최대공약수를 구함
    c = math.gcd(a,b)
    
    a = a//c
    b = b//c
    
    # 약분한 후, 분모에 2 또는 5만 있어야 유한소수임
    while b % 2 == 0:
        b = b // 2
        
    while b % 5 == 0:
        b = b // 5
    
    # 분모에 1만 남아있을때, 유한소수가 됨
    return 1 if b == 1 else 2