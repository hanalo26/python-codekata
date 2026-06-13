# 첫 번째로 나오는 음수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 알고리즘: 리스트(배열)
# 작성자: 백하은
# 작성일: 2026. 06. 13. 18:53:38

def solution(num_list):
    for idx, i in enumerate(num_list):
        if i < 0:
            return idx
        
    return -1