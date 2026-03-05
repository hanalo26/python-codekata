# 한 번만 등장한 문자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 03. 05. 09:44:24

def solution(s):
    answer_sub = []
    
    for i in set(s):
        if s.count(i) == 1:
            answer_sub += i
    
    answer = "".join(sorted(answer_sub))
    
    return answer