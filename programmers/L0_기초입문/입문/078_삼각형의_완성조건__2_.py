# 삼각형의 완성조건 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 19. 21:06:14

def solution(sides):
    answer = (2 * min(sides)) - 1
    return answer