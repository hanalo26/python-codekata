# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 04. 05. 18:13:23

def solution(s):
    answer = []
    
    for i in s.split():
        if i == 'Z':
            del answer[-1]
        else:
            answer.append(int(i))
    
    return sum(answer)