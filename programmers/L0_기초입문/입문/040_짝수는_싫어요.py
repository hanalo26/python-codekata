# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 28. 09:56:42

def solution(n):
    answer = []
    
    for i in range(1,n+1):
        if i % 2 != 0:
            answer.append(i)
    
    return answer