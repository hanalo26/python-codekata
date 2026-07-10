# 커피 심부름
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 07. 10. 22:13:17

def solution(order):
    answer = 0
    
    for menu in order:
        if "cafelatte" in menu:
            answer += 5000
        else:
            answer += 4500
    
    return answer