# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 26. 09:31:22

def solution(before, after):
    sorted_after = sorted(after)
    sorted_before = sorted(before)
    
    if sorted_before == sorted_after:
        return 1
    else:
        return 0