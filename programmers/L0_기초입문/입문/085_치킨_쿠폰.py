# 치킨 쿠폰
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 20. 10:25:16

def solution(chicken):
    if chicken > 0:
        return (chicken - 1) // 9
    else:
        return 0