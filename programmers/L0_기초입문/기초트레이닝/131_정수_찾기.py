# 정수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181840
# 알고리즘: 조건문 활용
# 작성자: 백하은
# 작성일: 2026. 06. 25. 20:14:55

def solution(num_list, n):
    for i in num_list:
        if i == n:
            return 1
        else:
            continue
    
    return 0