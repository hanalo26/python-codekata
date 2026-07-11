# 왼쪽 오른쪽
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 07. 11. 20:03:36

def solution(str_list):
    for idx, txt in enumerate(str_list):
        # l을 먼저 만났을 때
        if txt == "l":
            return str_list[:idx]
        
        # r을 먼저 만났을 때
        elif txt == "r":
            return str_list[idx+1:]

    # l, r이 존재하지 않을 때
    return []