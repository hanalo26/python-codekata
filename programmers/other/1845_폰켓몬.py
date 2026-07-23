# 폰켓몬
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 작성자: 백하은
# 작성일: 2026. 07. 23. 20:57:38

def solution(nums):
    # 박사님이 보유한 폰켓몬의 수
    n = len(nums)
    
    # 내가 데려올 수 있는 폰켓몬의 수
    me = n // 2
    
    # 박사님이 보유한 폰켓몬의 종류 수
    s = len(set(nums))
    
    # 내가 가질 수 있는 최대한의 폰켓몬 종류 수
    return min(me, s)