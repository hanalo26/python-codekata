# 올바른 괄호
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 작성자: 백하은
# 작성일: 2026. 07. 25. 18:56:26

def solution(s):
    opened = []
    
    for i in s:
        if i == "(":
            opened.append(i)
        elif opened: 
            opened.pop()
        else:
            return False
        
    if opened:
        return False     
            
    return True