# 뒤에서 5등까지
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181853
# 알고리즘: 함수(메서드)
# 작성자: 백하은
# 작성일: 2026. 06. 28. 18:42:24

def solution(num_list):
    
    # 오름차순으로 정렬
    sorted_num_list = sorted(num_list)
    
    answer = sorted_num_list[:5]
    
    return answer