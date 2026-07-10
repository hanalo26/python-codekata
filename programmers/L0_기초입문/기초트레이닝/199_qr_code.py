# qr code
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181903
# 알고리즘: 문자열
# 작성자: 백하은
# 작성일: 2026. 07. 10. 22:07:58

def solution(q, r, code):
    answer = ''
    
    for idx, txt in enumerate(code):
        if idx % q == r:
            answer += txt
    
    return answer