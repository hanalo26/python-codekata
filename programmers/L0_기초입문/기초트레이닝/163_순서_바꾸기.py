# 순서 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181891
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 02. 17:16:22

def solution(num_list, n):
    # n번째 원소 이후의 원소
    after_n = num_list[n:]
    
    # n번째 원소 이전의 원소
    before_n = num_list[:n]
    
    return after_n + before_n