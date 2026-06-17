# n 번째 원소부터
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181892
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 06. 17. 14:09:08

def solution(num_list, n):
    # n번째 원소는 인덱스로 (n - 1)
    answer = num_list[n-1:]
    
    return answer