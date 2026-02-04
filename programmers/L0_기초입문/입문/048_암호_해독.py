# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 04. 19:49:53

def solution(cipher, code):
    answer = ''
    
    for i in range(code-1, len(cipher),code):
        answer += cipher[i]
    
    return answer 