# 2 x n 타일링
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12900
# 작성자: 백하은
# 작성일: 2026. 07. 25. 22:28:53

# n은 만들고자 하는 직사각형의 가로 길이
# 내가 가진 블럭은 가로(w) = 2, 세로(h) = 1
# a가 가로로 놓은 블럭의 개수, b가 세로로 놓은 블럭의 개수라 하면 -> 2a+b = n

# n이 1 ~ 5일때를 모두 그려 보니 return값이 1, 2, 3, 5, 8
# -> n-2일 떄의 값 + n-1일 때의 값 = n일때의 값

# 반환해야 하는 값: 경우의 수를 1000,000,007으로 나눈 나머지

def solution(n):
    
    maps = [0]*(n+2) # n=1일때는 maps[2]가 안 만들어지기 때문에 더 크게 만듦
    
    maps[1] = 1
    maps[2] = 2
    
    # n >= 3이라면?
    if n >= 3:
        for i in range(3,n+1):
            maps[i] = (maps[i-2] + maps[i-1]) % 1000000007
    
    answer = maps[n]
    return answer