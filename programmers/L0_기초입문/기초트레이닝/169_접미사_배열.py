# 접미사 배열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181909
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 03. 15:50:00

def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        answer.append(my_string[i:])
        
    answer.sort()
        
    return answer