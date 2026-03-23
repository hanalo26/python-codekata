# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 03. 23. 10:08:24

def solution(array):
    text = "".join(map(str, array))
    return text.count('7')