# 뒤에서 5등 위로
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181852
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 06. 28. 18:36:42

def solution(num_list):
    
    sorted_num_list = sorted(num_list)
    
    answer = sorted_num_list[5:]
    
    return answer