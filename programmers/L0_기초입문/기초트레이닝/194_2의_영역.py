# 2의 영역
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181894
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 09. 15:55:17

def solution(arr):
    indices = [idx for idx, n in enumerate(arr) if n == 2]
    
    # 2가 존재하지 않을 때
    if not indices:
        return [-1]
    
    # 2가 존재할 때
    else:
        start_idx = indices[0]
        end_idx = indices[-1]

        return arr[start_idx:end_idx+1]