# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 06. 04. 21:57:43

def solution(num, total):
    # 등차수열 합 공식 중 처음과 끝을 알 때 사용하는 식을 전개해서 첫 번째 항(start)을 구함
    start = (total - sum(range(num))) // num
    return [i for i in range(start, start + num)]