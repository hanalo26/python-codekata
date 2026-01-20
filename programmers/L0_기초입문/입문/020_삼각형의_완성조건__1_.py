# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 20. 09:34:27

def solution(sides):
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if c < a + b:
        return 1
    else:
        return 2