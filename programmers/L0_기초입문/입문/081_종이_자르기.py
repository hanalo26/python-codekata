# 종이 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120922
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 28. 23:31:26

def solution(M, N):
    
    # M*N 크기의 종이를 잘라서 1*1 종이를 만들기 위한 가위질 횟수 = M*N-1
    answer = M * N - 1
    return answer