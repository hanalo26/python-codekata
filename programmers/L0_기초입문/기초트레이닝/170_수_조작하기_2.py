# 수 조작하기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181925
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 07. 06. 14:19:20

def solution(numLog):
    
    answer = ""
    
    for i in range(1,len(numLog)):
        diff = numLog[i] - numLog[i-1]
        
        if diff == 1:
            answer+= 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += "d"
        elif diff == -10:
            answer += "a"
            
    return answer