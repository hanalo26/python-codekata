# 멀리 뛰기
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 알고리즘: DP
# 작성자: 백하은
# 작성일: 2026. 08. 05. 12:47:43

def solution(n):
    if n <= 2:
        # n=1 -> (1칸)
        # n=2 -> (1칸, 1칸), (2칸)
        return n
    
    DP = [0] * (n+1)
    DP[1] = 1
    DP[2] = 2
    
    for i in range(3,n+1):
        DP[i] = (DP[i-1] + DP[i-2]) % 1234567
    
    return DP[n]