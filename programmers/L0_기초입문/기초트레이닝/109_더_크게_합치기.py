# 더 크게 합치기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181939
# 알고리즘: 연산
# 작성자: 백하은
# 작성일: 2026. 06. 13. 18:59:01

def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    return max(ab, ba)