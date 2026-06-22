# 콜라츠 수열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181919
# 알고리즘: 반복문
# 작성자: 백하은
# 작성일: 2026. 06. 23. 00:18:48

def solution(n):
    answer = []
    
    while n != 1:
        answer.append(n)
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n+1
    
    answer.append(n)
    
    return answer