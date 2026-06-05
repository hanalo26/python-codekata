# 분수의 덧셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 05. 22:01:09

import math

def solution(numer1, denom1, numer2, denom2):
    # 두 분수를 더한 값 - 분모끼리 곱해서 통분함
    combined_numer = numer1*denom2 + numer2*denom1
    combined_denom = denom1*denom2
    
    # 최대공약수 계산 - math 라이브러리의 .gcp() 사용
    gcd_val = math.gcd(combined_numer, combined_denom)
    
    return [combined_numer // gcd_val, combined_denom//gcd_val]