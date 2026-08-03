# 피보나치 수
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 알고리즘: DP
# 작성자: 백하은
# 작성일: 2026. 08. 03. 10:23:08

def solution(n):
    fibo = [0,1]
    
    for i in range(2, n+1):
        fibo.append((fibo[i-2]+fibo[i-1])%1234567)
        
    return fibo[n]