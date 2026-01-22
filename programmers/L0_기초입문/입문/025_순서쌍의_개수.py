# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 01. 22. 10:52:01

def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer

# a * b = n이라면 a,b는 n의 약수
# 1부터 n까지 모든 숫자를 조회해서 약수를 찾아내는 과정에서 (a,b), (b,a) 모두 포함되어 있음