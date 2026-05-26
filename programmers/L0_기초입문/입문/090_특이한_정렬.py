# 특이한 정렬
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120880
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 05. 26. 09:57:02

def solution(numlist, n):
    # numlist를 오름차순으로 정렬하되, lambda 함수를 써서 절댓값, -x 기준 순서로 정렬
    answer = sorted(numlist, key= lambda x: (abs(x-n), -x))
    
    return answer