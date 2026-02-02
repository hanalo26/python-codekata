# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 02. 23:10:32

def solution(my_string):
    answer = []
    
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
            
    answer.sort()
    
    return answer
            
