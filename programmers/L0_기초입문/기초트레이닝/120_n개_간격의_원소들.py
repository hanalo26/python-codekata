# n개 간격의 원소들
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181888
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 06. 21. 19:32:47

def solution(num_list, n):
    # 파이썬의 슬라이싱 문법 
    # 리스트[시작:끝:간격]
    answer = num_list[::n]
    return answer