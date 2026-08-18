# 괄호 회전하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 알고리즘: 스택, 문자열
# 작성자: 백하은
# 작성일: 2026. 08. 18. 19:00:29

def is_valid(s):
    stack = []
    
    # 올바른 괄호 짝꿍
    pair = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        # 여는 괄호는 스택에 추가하고, 닫는 괄호는 스택이 비어있거나 짝지어져 있는지 확인
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop() # 마지막 요소 삭제
            
    if len(stack) == 0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        # 슬라이싱을 사용해 회전 i를 기준으로 앞부분을 뒷부분에 이어 붙여서 왼쪽으로의 회전을 구현
        rotationed = s[i:] + s[:i]
        if is_valid(rotationed):
            answer+=1
    
    return answer