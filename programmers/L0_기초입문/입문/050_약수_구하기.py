# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 06. 09:20:15

def solution(n):
    measure = []
    
    for i in range(1, n+1):
        if n % i == 0:
            measure.append(i)
    
    answer = sorted(measure)
    
    return answer