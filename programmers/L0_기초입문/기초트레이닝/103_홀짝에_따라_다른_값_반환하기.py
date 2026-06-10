# 홀짝에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 알고리즘: 조건문
# 작성자: 백하은
# 작성일: 2026. 06. 10. 13:42:55

def solution(n):
    answer = 0
    
    # n이 홀수인 경우
    if n % 2 != 0:
        for i in range(1,n+1,2):
            answer += i
            
    # n이 짝수인 경우
    else:
        for j in range(2, n+1, 2):
            answer += j ** 2  # j의 제곱
    
    return answer