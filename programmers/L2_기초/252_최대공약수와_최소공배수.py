# 최대공약수와 최소공배수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 07. 15. 11:02:10

import math

def solution(n, m):
    # 최대공약수 계산
    gcd = math.gcd(n,m)
    
    # 최소공배수(lcm) 계산
    # = (두 수의 곱) // 최대공약수
    lcm = (n*m) // gcd
    
    return [gcd, lcm]
    
    