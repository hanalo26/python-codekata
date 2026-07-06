# 수 조작하기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 06. 15:06:35

def solution(n, control):
    for char in control:
        if char == 'w':
            n+=1
        elif char == 's':
            n-=1
        elif char == "d":
            n+=10
        elif char == "a":
            n-=10
            
    return n