# 올바른 괄호
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 작성자: 백하은
# 작성일: 2026. 07. 23. 22:17:00

# 올바른 괄호가 되기 위해서는 ( 등장 -> ) 등장
# 닫는 괄호가 나오기 전에 여는 괄호가 쌓여있어야 함 -> 만약에 없다면 False
# 모든 걸 다 순회하였음에도 불구하고, 여는 괄호가 남아있다면 False

def solution(s):
    opened = []
    
    for i in s:
        if i == "(":
            opened.append(i)
        elif opened:
                opened.pop() # 맨 뒤에 있는 요소 제거
        else:
            return False
            
    if opened:
        return False
    
    return True