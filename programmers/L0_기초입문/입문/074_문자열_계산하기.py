# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 09. 12:40:52

def solution(my_string):
    tokens = my_string.split()
    
    answer = int(tokens[0])
    
    # 연산자 위치에 따라 파싱
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        num = int(tokens[i+1])
        
        if operator == '+':
            answer += num
        else:
            answer -= num
            
    return answer
    
    return 