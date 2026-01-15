# 부족한 금액 계산하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 알고리즘: 수학
# 작성자: 백하은
# 작성일: 2026. 01. 16. 01:55:04

def solution(price, money, count):
    total_cost = price * (count*(count+1)//2)
    
    if total_cost > money:
        return total_cost - money

    return 0