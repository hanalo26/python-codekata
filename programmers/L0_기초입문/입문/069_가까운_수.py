# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 02. 11:33:16

def solution(array, n):
    
    # .sort(key=): 정렬 기준 지정, 주로 lambda 함수 사용 
    array.sort(key=lambda x:(abs(x-n), x))
    
    return array[0]