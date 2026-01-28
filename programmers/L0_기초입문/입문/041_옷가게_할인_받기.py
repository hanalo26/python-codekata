# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 28. 10:03:13

import math

def solution(price):
    if price >= 500000:
        final_price = price * 0.8
    elif price >= 300000:
        final_price = price * 0.9
    elif price >= 100000:
        final_price = price * 0.95 
    else:
        final_price = price
    
    return math.floor(final_price)