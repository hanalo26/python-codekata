# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 04. 21:58:24

def solution(num, total):
    # 전체 합(total)에서 0부터 늘어난 누적합을 뺀 뒤, 개수(num)로 나누어 첫 번째 항을 구함
    start = (total - sum(range(num))) // num
    return [i for i in range(start, start + num)]