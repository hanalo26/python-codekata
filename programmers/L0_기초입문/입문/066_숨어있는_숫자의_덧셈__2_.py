# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 03. 16. 10:01:31

import re

def solution(my_string):
    
    nums = re.findall(r'\d+', my_string)
    
    answer = 0
    
    for n in nums:
        answer += int(n)
    
    return answer