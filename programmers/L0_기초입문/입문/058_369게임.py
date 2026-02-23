# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 23. 09:45:08

def solution(order):
    order_str = str(order)
    
    answer = 0
    for i in order_str:
        if i in ['3', '6', '9']:
            answer += 1
            
    return answer