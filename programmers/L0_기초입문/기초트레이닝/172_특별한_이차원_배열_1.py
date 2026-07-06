# 특별한 이차원 배열 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181833
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 06. 14:36:15

def solution(n):
    # 모든 원소가 0으로 채워진 n x n 크기의 배열 생성 
    answer = [[0]*n for _ in range(n)]
    
    # i == j인 위치의 원소는 1로 변경
    for i in range(n):
        answer[i][i] = 1
    
    return answer