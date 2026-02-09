# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 09. 09:42:48

def solution(array):
    max_value = array[0]
    max_index = 0
    
    for index, i in enumerate(array):
        if i > max_value:
            max_value = i
            max_index = index

    return [max_value, max_index]