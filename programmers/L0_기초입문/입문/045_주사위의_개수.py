# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 02. 22:14:58

def solution(box, n):
    box_width = box[0]
    box_length = box[1]
    box_height = box[2]
    
    a = box_width // n
    b = box_length // n
    c = box_height // n
    
    answer = a*b*c
    
    return answer