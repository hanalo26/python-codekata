# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 백하은
# 작성일: 2026. 02. 11. 14:01:30

def solution(age):
    answer = ''
    alphabet = 'abcdefghij'
    
    for i in str(age):
        i = int(i)
        answer += alphabet[i]
        
    return answer